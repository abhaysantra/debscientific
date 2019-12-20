from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Max, Min
import json
from debadmin.models import user_addon_cart_item, user_cart_item, user_wish_list, slider, brand, banner, product, product_image, category, contactUs, sub_product

def index(request):
    slider_list = slider.objects.filter(status='active')
    brand_list = brand.objects.filter(status='active')
    product_list = product.objects.filter(product_status='active')
    latest_product_list = product.objects.filter(product_status='active').order_by('-id')
    banner_det = banner.objects.all()

    context = common_data(request)
    context['slider_list'] = slider_list
    context['brand_list'] = brand_list
    context['product_list'] = product_list
    context['latest_product_list'] = latest_product_list
    context['banner_det'] = banner_det
    context['product_list'] = product_list

    return render(request, 'home/home.html',context)




def common_data(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        addon_cart_list = user_addon_cart_item.objects.filter(user_id=user_session_id)
        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
        wish_list = user_wish_list.objects.raw('SELECT * FROM debadmin_user_wish_list c JOIN debadmin_product p ON c.product_id = p.id WHERE c.user_id = %s'%user_session_id)
        product_wish_list = [obj.product_id for obj in wish_list]

        session_cart_list = []
        total_cart_item = len(list(cart_list))
        total_wish_item = len(list(wish_list))
        total_cart_price = 0
        total_shipping_charge = 0
        total_addon_cart_price = 0
        total_cart_save_price = 0
        for cart_list_row in cart_list:
            cart_price = cart_list_row.cart_item_qty * cart_list_row.cart_sell_price
            cart_save_price = cart_list_row.cart_mrp_price*cart_list_row.cart_item_qty - cart_price
            total_cart_price += cart_price
            total_cart_save_price += cart_save_price

            # for addon product list
            jsonDec = json.decoder.JSONDecoder()
            addon_id = jsonDec.decode(cart_list_row.addon_id_list)
            if int(addon_id.strip()) == 0:
                addon_price = 0
            else:
                addon_obj = sub_product.objects.filter(id=addon_id)
                addon_price = addon_obj[0].sub_product_price
            total_cart_price +=addon_price

        # if addon_cart_list:
        #     for addon_cart_row in addon_cart_list:
        #         total_addon_cart_price += addon_cart_row.addon_item_sell_price
        
        # total_cart_price += total_addon_cart_price


    else:
        total_cart_price = 0
        total_shipping_charge = 0
        total_cart_save_price = 0

        # this is for testing purpose
        # del request.session['deb_cart_item'] # temporarily to avoid deb_cart_item dictionary
        if 'deb_cart_item' in request.session:
            session_cart_list = request.session['deb_cart_item']
            # keys=tuple(session_cart_list.keys())
            keys = session_cart_list.keys()
            # product_ids = []
            # for key in keys:
            #     if key.find('_') > 0:
            #         product_ids.append(key.split('_')[0])
            #     else:
            #         product_ids.append(key)
            # print('product_ids list: ',product_ids)
            # product_ids = tuple(product_ids)
            # print('product_ids tuple: ',product_ids)

            # print('session length : ',len(session_cart_list))
            
            # if len(session_cart_list) > 1:
            #     cart_list_test = product.objects.raw('SELECT * FROM debadmin_product WHERE id IN %s' % (product_ids,) )
            # if len(session_cart_list) == 1:
            #     cart_list_test = product.objects.raw('SELECT * FROM debadmin_product WHERE id = %s' %product_ids )
            
            # modifying this cart_list for product_id as for non-loggedin user there is no product_id.
            # Instead of product_id it is product_id_addon_id_list
            cart_list = []
            for key in keys:
                # print('..................key is debadmin_cart : ',key)
                each_cart_dict = {}
                product_id = key.split('_')[0].strip()
                product_obj = product.objects.filter(id=int(product_id))[0]
                each_cart_dict['id'] = product_obj.id
                each_cart_dict['product_slug'] = product_obj.product_slug
                each_cart_dict['sell_price'] = product_obj.sell_price
                each_cart_dict['quantity'] = int(session_cart_list[key])
                each_cart_dict['product_name'] = product_obj.product_name
                # each_cart_dict['cart_item_qty'] = 3

                each_cart_dict['total_price'] = product_obj.sell_price * int(session_cart_list[key])
                each_cart_dict['product_id_addon_id_list'] = key

                cart_list.append(each_cart_dict)

            if len(session_cart_list) == 0:
                cart_list = []

            # calculate total cart price
            for key in keys:
                product_qty = session_cart_list[key]
                product_id = key.split('_')[0]
                product_obj = product.objects.filter(id=int(product_id))[0]
                product_sell_price = product_obj.sell_price
                total_product_price = product_qty*product_sell_price

                # there are some products which do not have any addon
                addon_id = key.split('_')[1]
                total_addon_product_price = 0
                if int(addon_id.strip()) == 0:
                    total_cart_price += total_product_price
                else:
                    addon_product_obj = sub_product.objects.filter(id=int(addon_id))[0]
                    addon_product_price = addon_product_obj.sub_product_price
                    # for addon_id in addon_ids:
                    #     addon_product_obj = sub_product.objects.filter(id=int(addon_id))
                    #     addon_product_price = addon_product_obj[0].sub_product_price
                    #     total_addon_product_price += addon_product_price
                    total_cart_price += total_product_price + addon_product_price

        else:
            session_cart_list = []
            cart_list = []

        wish_list = []
        product_wish_list = []

        total_cart_item = len(list(cart_list))
        total_wish_item = len(list(wish_list))
        
        # print('session_cart_list : ',session_cart_list['1'])
        # for cart_list_row in cart_list:
        #     product_id = cart_list_row.id
        #     cart_price = session_cart_list[str(product_id)] * cart_list_row.sell_price
        #     total_cart_price += cart_price

        


    
    

    all_category = category.objects.filter(category_status='active')
    all_sub_category = category.objects.filter(sub_category=0,category_status='active')
    all_parent_category = category.objects.filter(parent_category=0,category_status='active')
    contact_us_det = contactUs.objects.all()
    product_image_list = product_image.objects.raw('SELECT * FROM debadmin_product_image GROUP BY product_id')
    price_list = product.objects.filter(price_available='yes').aggregate(Max('sell_price'), Min('sell_price'))
    
    context = {
                'all_category':all_category,
                'all_sub_category':all_sub_category,
                'all_parent_category':all_parent_category,
                'product_image_list':product_image_list,
                'contact_us_det':contact_us_det,
                'cart_list':cart_list,
                'total_cart_item':total_cart_item,
                'total_cart_price':total_cart_price,
                'total_cart_save_price':total_cart_save_price,
                'total_shipping_charge':total_shipping_charge,
                'user_wish_list':wish_list,
                'total_wish_item':total_wish_item,
                'product_wish_list':product_wish_list,
                'session_cart_list':session_cart_list,
                'price_list':price_list,
                }

    return context