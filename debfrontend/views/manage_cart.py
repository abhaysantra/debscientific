from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import home, manage_login
from debadmin.models import user_cart_item, user_addon_cart_item, sub_product, pincode_service, slider, brand, product, product_image, category, contactUs
dict_cart_item = {}

def add_to_cart(request):
    product_id = request.POST['product_id']
    pro_qty = request.POST['product_qty']
    pro_det = product.objects.filter(id=product_id)[0]
    pro_mrp_price = pro_det.mrp_price
    pro_discount = pro_det.discount
    pro_sell_price = pro_det.sell_price

    # without login cart dictionary

    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        check_cart = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item WHERE user_id = %s AND cart_item_id = %s'%(user_session_id,product_id))

        if len(list(check_cart)):
            check_cart[0].cart_item_qty += 1
            check_cart[0].save(update_fields=['cart_item_qty']) 
        else:
            cart_info = user_cart_item(
                        user_id=user_session_id,
                        cart_item_id=product_id,
                        cart_mrp_price=pro_mrp_price,
                        cart_item_qty=pro_qty,
                        cart_discount=pro_discount,
                        cart_sell_price=pro_sell_price,
                        )
            cart_info.save()

    else:
        if 'deb_cart_item' in request.session:
            dict_cart_item = request.session['deb_cart_item']
            if product_id not in dict_cart_item.keys():
                dict_cart_item[product_id]=int(pro_qty)
            else:
                dict_cart_item[product_id]=dict_cart_item[product_id] + 1

            request.session['deb_cart_item'] = dict_cart_item

        else:
            dict_cart_item={}
            dict_cart_item[product_id]=int(pro_qty)
            request.session['deb_cart_item'] = dict_cart_item
        
        
    # print('cart item list : ',dict_cart_item)   
    return JsonResponse({'result': '1'})

def direct_buy_now(request):
    product_id = request.POST['product_id']
    pro_qty = request.POST['product_qty']

    # without login cart dictionary
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        # check_cart_for_addon_list = user_cart_item.objects.filter(cart_item_id=product_id,user_id=user_session_id)
        check_cart_for_addon_list = user_cart_item.objects.filter(user_id=user_session_id)
        if len(check_cart_for_addon_list):
            print('data present')
            result = 1
        else:
            print('there is no data..')
            result = 0
        return JsonResponse({'result': result})

    # Case for non-logged-in user : when going to "buy now" directly, there should be a checking if addon_product already there or not. 
    else:
        if 'deb_cart_item' in request.session:
            dict_cart_item = request.session['deb_cart_item']
            product_id_addon_id_list = dict_cart_item.keys()
            for each_product_id_addon_id in product_id_addon_id_list:
                if each_product_id_addon_id.find('_') > 0:
                    return JsonResponse({'result': 1})
        return JsonResponse({'result': 0})


    # old-case when buy through only product_id
    # else:
    #     if 'deb_cart_item' in request.session:
    #         dict_cart_item = request.session['deb_cart_item']
    #         if product_id not in dict_cart_item.keys():
    #             dict_cart_item[product_id]=int(pro_qty)
    #         else:
    #             dict_cart_item[product_id]=dict_cart_item[product_id] + 1

    #         request.session['deb_cart_item'] = dict_cart_item

    #     else:
    #         dict_cart_item={}
    #         dict_cart_item[product_id]=int(pro_qty)
    #         request.session['deb_cart_item'] = dict_cart_item        
    # print('cart item list : ',dict_cart_item)   
    # return JsonResponse({'result': '1'})


def update_cart_item_qty(request):
    update_cart_id = request.POST['cart_id']
    qty = request.POST['qty']
    # user_session_id = request.session['user_session_id']
    try:
        cart_info = user_cart_item.objects.filter(id=update_cart_id)[0]
        cart_info.cart_item_qty = qty
        cart_info.save(update_fields=['cart_item_qty'])
        result = 1
    except Exception as e:
        print('There may be some issue : ',e)
        result = 0

    return JsonResponse({'result': result})

def delete_cart_item(request):
    delete_cart_id = request.POST['cart_id']
    try:
        user_addon_cart_item.objects.filter(cart_id=delete_cart_id).delete()
        cart_info = user_cart_item.objects.filter(id=delete_cart_id)[0]
        cart_info.delete()
        result = 1
    except Exception as e:
        print('There may be some issue : ',e)
        result = 0

    return JsonResponse({'result': result})

def view_cart(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
        
        if len(cart_list)==0:
            return redirect(home.index)
    
        context = home.common_data(request)
    
        return render(request, 'view_cart.html',context)
    else:
        if 'deb_cart_item' in request.session:
            session_cart_list = request.session['deb_cart_item']
            # product_ids=tuple(session_cart_list.keys())

            keys = session_cart_list.keys()
            # print('product_ids along with addon_ids : ',keys,'session_cart_list : ',session_cart_list)
            product_ids = []
            for key in keys:
                product_ids.append(key.split('_')[0])
            product_ids = tuple(product_ids)
            print('product_ids tuple: ',product_ids)
            
            if len(session_cart_list) > 1:
                cart_list = product.objects.raw('SELECT * FROM debadmin_product WHERE id IN %s' % (product_ids,) )
            if len(session_cart_list) == 1:
                cart_list = product.objects.raw('SELECT * FROM debadmin_product WHERE id = %s' %product_ids )
            if len(session_cart_list) == 0:
                cart_list = []
        
            if len(cart_list)==0:
                return redirect(home.index)
        
            context = home.common_data(request)
            return render(request, 'view_cart.html',context)
        else:
            return redirect(home.index)
        
        # return render(request, 'view_cart_non_loggedin.html',context)

def order_summary(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
    else:
        return redirect(manage_login.login)

    if len(cart_list)==0:
        return redirect(home.index)
    
    context = home.common_data(request)
    
    return render(request, 'order_summary.html',context)

def check_pincode_service(request):
    pin = request.POST['pincode']
    check_pin = pincode_service.objects.filter(pincode=pin, status='active')
    if check_pin:
        result = 'yes'
        # special case after checking delivery status of pincode
        request.session['pincode'] = pin
    else:
        result = 'no'
    return JsonResponse({'result':result})

def session_cart_item_delete(request):
    product_id_addon_id_list = str(request.POST['product_id_addon_id_list'])
    session_cart_list = request.session['deb_cart_item']
    print('session_cart_list.keys : ',session_cart_list.keys(), 'to be deleted id :',product_id_addon_id_list)
    if product_id_addon_id_list in session_cart_list.keys():
        del session_cart_list[product_id_addon_id_list]

    # print('after delete:',session_cart_list)
    request.session['deb_cart_item'] = session_cart_list
    return JsonResponse({'result': product_id_addon_id_list})


def update_sess_cart_item_qty(request):
    sess_cart_id_with_addon_product = request.POST['sess_cart_id_with_addon_product']
    qty = request.POST['qty']
    session_cart_list = request.session['deb_cart_item']
    
    if sess_cart_id_with_addon_product in session_cart_list.keys():
        session_cart_list[sess_cart_id_with_addon_product]= int(qty)

    request.session['deb_cart_item'] = session_cart_list
    return JsonResponse({'result': sess_cart_id_with_addon_product})

def add_single_to_cart(request):
    print('add_single_to_cart : ')
    product_id = request.POST['product_id']
    pro_qty = request.POST['product_qty']
    addon_product_list = request.POST['addon_product_list']
    print(product_id,pro_qty,addon_product_list)
    pro_det = product.objects.filter(id=product_id)[0]
    pro_mrp_price = pro_det.mrp_price
    pro_discount = pro_det.discount
    pro_sell_price = pro_det.sell_price

    # without login cart dictionary

    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        # check_cart = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item WHERE user_id = %s AND cart_item_id = %s'%(user_session_id,product_id))
        # print('addon_product_list : ',addon_product_list)
        
        check_cart = user_cart_item.objects.filter(user_id=user_session_id,cart_item_id = product_id, addon_id_list=json.dumps(addon_product_list))
        # print('check_cart : ',check_cart,'with addon :',addon_product_list)
        # print('addon_product_list : ',addon_product_list)
        if len(list(check_cart)):
            cart_id = check_cart[0].id
            check_cart[0].cart_item_qty += int(pro_qty)
            check_cart[0].save(update_fields=['cart_item_qty'])
        else:
            
            addon_id_list = json.dumps(addon_product_list)
            print('json serialised addon id list :',addon_id_list)

            cart_info = user_cart_item(
                        user_id=user_session_id,
                        cart_item_id=product_id,
                        cart_mrp_price=pro_mrp_price,
                        cart_item_qty=pro_qty,
                        cart_discount=pro_discount,
                        cart_sell_price=pro_sell_price,
                        addon_id_list = addon_id_list,
                        )
            cart_info.save()
            cart_id = cart_info.id

            if addon_product_list:
                    sub_product_det_list = sub_product.objects.filter(id=addon_product_list)
                    print('sub_product_det_list : ',sub_product_det_list)
                    for addon_product_row in sub_product_det_list:
                        addon_pro_info = user_addon_cart_item(
                                                        user_id = user_session_id,
                                                        product_id = product_id,
                                                        cart_id = cart_id,
                                                        addon_item_id = addon_product_row.id,
                                                        addon_item_sell_price = addon_product_row.sub_product_price,
                                                            )
                        addon_pro_info.save()

    else:
        # print('inside non logged in user..')
        print('addon_product_list :',addon_product_list)
        # addon_id_string = '_'
        # addon_id_string  = addon_id_string.join(addon_product_list)
        # print('addon_id_string :',addon_id_string)

        # del request.session['deb_cart_item']
        if 'deb_cart_item' in request.session:
            dict_cart_item = request.session['deb_cart_item']
            print('deb_cart_item exists ...details : ',dict_cart_item)

            key = product_id+'_' + addon_product_list
            if key not in dict_cart_item.keys():
                dict_cart_item[key]=int(pro_qty)
            else:
                dict_cart_item[key]=dict_cart_item[key] + int(pro_qty)

            request.session['deb_cart_item'] = dict_cart_item

        else:
            print('deb_cart_item does not exist ...')
            dict_cart_item={}
            #making dict_cart_item key as combination of product_id_addon_id_list instead of ONLY product id
            # as user can not buy any product without addon product
            key = product_id+'_'+ addon_product_list
            dict_cart_item[key]=int(pro_qty)
            request.session['deb_cart_item'] = dict_cart_item
            print('deb_cart_item : ',request.session['deb_cart_item'])
                
    # print('cart item list : ',dict_cart_item)   
    return JsonResponse({'result': '1'})

def get_addon_product_list(request):
    product_id = request.POST['product_id']
    print('get_addon_product_list : product_id :',product_id)
    addon_product_list = sub_product.objects.filter(product_id=product_id)
    print('addon_product_list : ',addon_product_list)
    if addon_product_list:
        return JsonResponse({'result': 1})
    else:
        return JsonResponse({'result': 0})