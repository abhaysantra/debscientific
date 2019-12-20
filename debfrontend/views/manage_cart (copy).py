from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
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


def update_cart_item_qty(request):
    update_cart_id = request.POST['cart_id']
    qty = request.POST['qty']
    # user_session_id = request.session['user_session_id']

    cart_info = user_cart_item.objects.filter(id=update_cart_id)[0]
    cart_info.cart_item_qty = qty
    cart_info.save(update_fields=['cart_item_qty'])

    return JsonResponse({'result': '1'})

def delete_cart_item(request):
    delete_cart_id = request.POST['cart_id']

    user_addon_cart_item.objects.filter(cart_id=delete_cart_id).delete()
    cart_info = user_cart_item.objects.filter(id=delete_cart_id)[0]
    cart_info.delete()
    

    return JsonResponse({'result': '1'})



def view_cart(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
    else:
        session_cart_list = request.session['deb_cart_item']
        product_ids=tuple(session_cart_list.keys())
        
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
    else:
        result = 'no'
    return JsonResponse({'result':result})

def session_cart_item_delete(request):
    product_id = str(request.POST['product_id'])
    session_cart_list = request.session['deb_cart_item']
    if product_id in session_cart_list.keys():
        # print('Enter if')
        del session_cart_list[product_id]

    # print('after delete:',session_cart_list)
    request.session['deb_cart_item'] = session_cart_list
    return JsonResponse({'result': product_id})


def update_sess_cart_item_qty(request):
    product_id = request.POST['sess_cart_id']
    qty = request.POST['qty']
    session_cart_list = request.session['deb_cart_item']
    
    if product_id in session_cart_list.keys():
        session_cart_list[product_id]= int(qty)

    request.session['deb_cart_item'] = session_cart_list
    # print('sesssssssssssllllsssss:',session_cart_list)
    return JsonResponse({'result': product_id})




def add_single_to_cart(request):
    product_id = request.POST['product_id']
    pro_qty = request.POST['product_qty']
    addon_product_list = request.POST.getlist('addon_product_list[]')
    pro_det = product.objects.filter(id=product_id)[0]
    pro_mrp_price = pro_det.mrp_price
    pro_discount = pro_det.discount
    pro_sell_price = pro_det.sell_price

    # without login cart dictionary

    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        check_cart = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item WHERE user_id = %s AND cart_item_id = %s'%(user_session_id,product_id))
        

        if len(list(check_cart)):
            cart_id = check_cart[0].id
            check_cart[0].cart_item_qty += int(pro_qty)
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
            cart_id = cart_info.id

        if addon_product_list:
            sub_product_det_list = sub_product.objects.filter(id__in=addon_product_list)
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
        if 'deb_cart_item' in request.session:
            dict_cart_item = request.session['deb_cart_item']
            if product_id not in dict_cart_item.keys():
                dict_cart_item[product_id]=int(pro_qty)
            else:
                dict_cart_item[product_id]=dict_cart_item[product_id] + int(pro_qty)

            request.session['deb_cart_item'] = dict_cart_item

        else:
            dict_cart_item={}
            dict_cart_item[product_id]=int(pro_qty)
            request.session['deb_cart_item'] = dict_cart_item
        
        
    # print('cart item list : ',dict_cart_item)   
    return JsonResponse({'result': '1'})

