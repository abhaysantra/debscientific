from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.core import serializers
import uuid
from random import randint
from . import home,manage_login
from debadmin.models import adminUser,user_wish_list, online_payment_details,user_addon_cart_item, addon_order, order, order_details, billing_address, user_address
from debadmin.models import order_address, user_cart_item, slider, brand, product, product_image, category, contactUs, countries, states, cities

def delivery_address(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        pincode = request.session['pincode']
        # print('pincode : ',pincode)

        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
    else:
        return redirect(manage_login.login)

    if len(cart_list)==0:
        return redirect(home.index)

    billing_address = adminUser.objects.filter(id=user_session_id,user_type_id='2')[0]
    delivery_address = user_address.objects.filter(user_id=user_session_id,is_default='yes')

    if delivery_address:
        delivery_address = delivery_address[0]
        #### check checked pincode and delivery address pincode are same or not 
        # if not same then update it
        # there could be something else: need to check this condition
        delivery_address.pincode = pincode
        delivery_address.save(update_fields=['pincode',])


    else:
        delivery_address = []

    all_countries = countries.objects.all()
    all_states = states.objects.filter(country_id = billing_address.country)
    all_cities = cities.objects.filter(state_id = billing_address.state)

    # for delivery address
    if delivery_address:
        all_states_of_delivery_address = states.objects.filter(country_id = delivery_address.country)
        all_cities_of_delivery_address = cities.objects.filter(state_id = delivery_address.state)
    else:
        all_states_of_delivery_address = []
        all_cities_of_delivery_address = []

    context = home.common_data(request)
    context['billing_address'] = billing_address 
    context['delivery_address'] = delivery_address
    context['pincode'] = pincode
    context['all_countries'] = all_countries
    context['all_states'] = all_states
    context['all_cities'] = all_cities

    # for delivery address
    context['all_states_of_delivery_address'] = all_states_of_delivery_address
    context['all_cities_of_delivery_address'] = all_cities_of_delivery_address

    
    return render(request, 'delivery_address.html',context)


def get_default_delivery_add(request):
    response_data = {}
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        delivery_address = user_address.objects.filter(user_id=user_session_id,is_default='yes')
        
        if delivery_address:
            delivery_address = delivery_address[0]
            response_data['deli_name'] = delivery_address.full_name
            response_data['deli_ph'] = delivery_address.mobile_number
            response_data['deli_email'] = delivery_address.email
            response_data['deli_country'] = delivery_address.country
            response_data['deli_state'] = delivery_address.state
            response_data['deli_city'] = delivery_address.city
            response_data['deli_pincode'] = delivery_address.pincode
            response_data['deli_landmark'] = delivery_address.landmark
            response_data['deli_gst_no'] = delivery_address.gst_no
            response_data['deli_address'] = delivery_address.address
        

    return JsonResponse(response_data)


def submit_billing_address(request):
    user_session_id = request.session['user_session_id']

    bill_name = request.POST['bill_name']
    bill_ph = request.POST['bill_ph']
    bill_email = request.POST['bill_email']
    bill_country = request.POST['bill_country']
    bill_state = request.POST['bill_state']
    bill_city = request.POST['bill_city']
    bill_pincode = request.POST['bill_pincode']
    bill_landmark = request.POST['bill_landmark']
    bill_gst_no = request.POST['bill_gst_no']
    bill_address = request.POST['bill_address']


    deli_name = request.POST['deli_name']
    deli_ph = request.POST['deli_ph']
    deli_email = request.POST['deli_email']
    deli_country = request.POST['deli_country']
    deli_state = request.POST['deli_state']
    deli_city = request.POST['deli_city']
    deli_pincode = request.POST['deli_pincode']
    deli_landmark = request.POST['deli_landmark']
    deli_gst_no = request.POST['deli_gst_no']
    deli_address = request.POST['deli_address']

    user_update_info = adminUser.objects.filter(id=user_session_id)
    if user_update_info:
        user_update_info = user_update_info[0]
        user_update_info.country = bill_country
        user_update_info.state = bill_state
        user_update_info.city = bill_city
        user_update_info.gst_no = bill_gst_no
        user_update_info.address = bill_address
        user_update_info.pin_code = bill_pincode
        user_update_info.landmark = bill_landmark
        user_update_info.modified_by = user_session_id
        user_update_info.modified_date = datetime.now().date()

        user_update_info.save(update_fields=['country','state','city','landmark','gst_no','address','pin_code','modified_by','modified_date'])

    # del request.session['bill_address_session_id']
    if 'bill_address_session_id' in request.session:
        bill_address_session_id = request.session['bill_address_session_id']
        print('bill_address_session_id : ',bill_address_session_id,'user_session_id : ',user_session_id)
        update_bill_info = billing_address.objects.filter(id=bill_address_session_id,user_id=user_session_id)
        if update_bill_info:
            update_bill_obj = update_bill_info[0]
            update_bill_obj.full_name=bill_name
            update_bill_obj.email=bill_email
            update_bill_obj.mobile_number=bill_ph
            update_bill_obj.pincode=bill_pincode
            update_bill_obj.country=bill_country
            update_bill_obj.state=bill_state
            update_bill_obj.city=bill_city
            update_bill_obj.landmark=bill_landmark
            update_bill_obj.gst_no=bill_gst_no
            update_bill_obj.address=bill_address

            update_bill_obj.save(update_fields=['full_name','email','mobile_number','pincode','country','state','city','landmark','gst_no','address'])
        else:
            create_new_billing_address(request, user_session_id,bill_name,bill_email,bill_ph,bill_pincode,bill_country,bill_state,bill_city,bill_landmark,bill_gst_no,bill_address)

    else:
        create_new_billing_address(request, user_session_id,bill_name,bill_email,bill_ph,bill_pincode,bill_country,bill_state,bill_city,bill_landmark,bill_gst_no,bill_address)


    exist_deli_address_info = user_address.objects.filter(user_id=user_session_id,is_default='yes')
    # print('deli address: ',exist_deli_address_info)

    if exist_deli_address_info:
        exist_deli_address_info = exist_deli_address_info[0]
        exist_deli_address_info.full_name=deli_name
        exist_deli_address_info.email=deli_email
        exist_deli_address_info.mobile_number=deli_ph
        exist_deli_address_info.pincode=deli_pincode
        exist_deli_address_info.country=deli_country
        exist_deli_address_info.state=deli_state
        exist_deli_address_info.city=deli_city
        exist_deli_address_info.landmark=deli_landmark
        exist_deli_address_info.gst_no=deli_gst_no
        exist_deli_address_info.address=deli_address
        exist_deli_address_info.modified_date=datetime.now().date()
        exist_deli_address_info.modified_by=user_session_id

        exist_deli_address_info.save(update_fields=['full_name','email','mobile_number','pincode','country','state','city','landmark','gst_no','address','modified_date','modified_by'])

    else:
        delivery_address_info = user_address(
                                        user_id=user_session_id,
                                        full_name=deli_name,
                                        email=deli_email,
                                        mobile_number=deli_ph,
                                        pincode=deli_pincode,
                                        country=deli_country,
                                        state=deli_state,
                                        city=deli_city,
                                        landmark=deli_landmark,
                                        gst_no=deli_gst_no,
                                        address=deli_address,
                                        is_default='yes',
                                        created_date=datetime.now().date(),
                                        created_by=user_session_id,
                                        )
        delivery_address_info.save()


    return JsonResponse({'result':'1'})

def create_new_billing_address(request, user_session_id,bill_name,bill_email,bill_ph,bill_pincode,bill_country,bill_state,bill_city,bill_landmark,bill_gst_no,bill_address):
    billing_address_info = billing_address(
                                    user_id=user_session_id,
                                    full_name=bill_name,
                                    email=bill_email,
                                    mobile_number=bill_ph,
                                    pincode=bill_pincode,
                                    country=bill_country,
                                    state=bill_state,
                                    city=bill_city,
                                    landmark=bill_landmark,
                                    gst_no=bill_gst_no,
                                    address=bill_address,
                                    created_date=datetime.now().date(),
                                    created_by=user_session_id,
                                    )
    billing_address_info.save()
    bill_address_id = billing_address_info.id
    request.session['bill_address_session_id'] = bill_address_id    

def place_order(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
    else:
        return redirect(manage_login.login)
    
    if len(cart_list)==0:
        return redirect(home.index)

    billing_address = adminUser.objects.filter(id=user_session_id,user_type_id='2')[0]
    delivery_address = user_address.objects.filter(user_id=user_session_id,is_default='yes')

    if delivery_address:
        delivery_address = delivery_address[0]
    else:
        delivery_address = []
    
    context = home.common_data(request)
    context['billing_address'] = billing_address 
    context['delivery_address'] = delivery_address 

    return render(request, 'place_order.html',context)

def payment(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        user_detail = adminUser.objects.filter(id=user_session_id)
        cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
        
        # order_info = order.objects.all()
        # last_order= order.objects.order_by('-id')
        # order_count = len(list(order_info)) + 1
        # date = datetime.now().date()
        # if last_order:
        #     order_id = int(last_order[0].id) + 1
        # else:
        #     order_id = 1
        # uniq_order_id = 'DEB-ORDER-' + str(date.day) + str(date.month) + str(date.year) + str(order_count) + '-' + str(order_id)
        # print('uniqqqqqqqqqqqqqqqqqqq:',uniq_order_id)
    else:
        return redirect(manage_login.login)
    
    if len(cart_list)==0:
        return redirect(home.index)
   
    context = home.common_data(request)
    context['user_detail'] = user_detail
    # context['uniq_order_id'] = uniq_order_id

    return render(request, 'payment.html',context)


def order_submit_action(request):
    payment_method = request.POST['payment_type']

    if payment_method == 'online':
        payment_id = request.POST['razorpay_payment_id']
        payment_status = 'paid'
    else:
        payment_status = 'unpaid'
    
    user_session_id = request.session['user_session_id']
    billing_address_id = request.session['bill_address_session_id']
    addon_cart_list = user_addon_cart_item.objects.filter(user_id=user_session_id)
    deli_address_info = user_address.objects.filter(user_id=user_session_id,is_default='yes')[0] 
    deli_address_id = deli_address_info.id
    cart_list = user_cart_item.objects.raw('SELECT * FROM debadmin_user_cart_item c JOIN debadmin_product p ON c.cart_item_id = p.id WHERE c.user_id = %s'%user_session_id)
    total_cart_price = 0
    total_cart_save_price = 0
    sub_total_price = 0
    total_addon_cart_price = 0
    for cart_list_row in cart_list:
        cart_price = cart_list_row.cart_item_qty * cart_list_row.cart_sell_price
        cart_save_price = cart_list_row.cart_mrp_price*cart_list_row.cart_item_qty - cart_price
        sub_total_price += cart_list_row.cart_mrp_price*cart_list_row.cart_item_qty
        total_cart_price += cart_price
        total_cart_save_price += cart_save_price

    if addon_cart_list:
            for addon_cart_row in addon_cart_list:
                total_addon_cart_price += addon_cart_row.addon_item_sell_price

    total_cart_price += total_addon_cart_price
    sub_total_price += total_addon_cart_price

    order_shipping_charge = 0
    order_total_price = total_cart_price + order_shipping_charge

    order_info = order(
                    order_customer_id = user_session_id,
                    order_total_price = order_total_price,
                    order_discount = total_cart_save_price,
                    order_sub_total_price = sub_total_price,
                    order_shipping_charge = order_shipping_charge,
                    payment_method = payment_method,
                    payment_status = payment_status,
                    order_created_date = datetime.now().date(),
                    )
    order_info.save()
    order_id = order_info.id


    if payment_method == 'online':
        payment_info = online_payment_details(
                                        user_id = user_session_id,
                                        order_id = order_id,
                                        payment_id = payment_id,
                                        pay_amount = order_total_price,
                                        payment_date = datetime.now().date(),
                                        )
        payment_info.save()

    for cart_row in cart_list:
        order_details_info = order_details(
                                    order_id = order_id,
                                    customer_id = user_session_id,
                                    order_product_id = cart_row.cart_item_id,
                                    addon_product_id_list = cart_row.addon_id_list,
                                    product_seller_id = '1',
                                    order_product_mrp = cart_row.cart_mrp_price,
                                    order_product_discount = cart_row.cart_discount,
                                    order_product_price = cart_row.cart_sell_price,
                                    order_product_qty = cart_row.cart_item_qty,
                                    order_created_date = datetime.now().date(),
                                        )
        order_details_info.save()

    order_address_info = order_address(
                                user_id = user_session_id,
                                order_id = order_id,
                                deli_address_id = deli_address_id,
                                bill_address_id = billing_address_id,
                                    )
    order_address_info.save()


    if addon_cart_list:
            for addon_cart_row in addon_cart_list:
                addon_order_info = addon_order(
                                        order_id=order_id,
                                        user_id=user_session_id,
                                        product_id=addon_cart_row.product_id,
                                        addon_product_id=addon_cart_row.addon_item_id,
                                        addon_product_price=addon_cart_row.addon_item_sell_price,
                                            )
                addon_order_info.save()

    update_bill_info = billing_address.objects.filter(id=billing_address_id,user_id=user_session_id)[0]
    update_bill_info.order_id = order_id
    update_bill_info.save(update_fields=['order_id'])

    # random order id and track id generation
    random_code = randint(000000,999999)
    random_char = str(uuid.uuid4().hex[0:4])
    order_unique_id = 'DEB-'+ str(random_code) + str(random_char) + '-' + str(order_id)
    order_track_id = str(uuid.uuid4().hex[0:10])
    # print('order_track_id : ',order_track_id, 'order_unique_id :',order_unique_id )

    update_order_info = order.objects.filter(id=order_id)[0]
    update_order_info.order_unique_id = order_unique_id
    update_order_info.order_track_id = order_track_id
    update_order_info.save(update_fields=['order_unique_id','order_track_id'])


    del request.session['bill_address_session_id']
    user_cart_item.objects.filter(user_id=user_session_id).delete()
    user_addon_cart_item.objects.filter(user_id=user_session_id).delete()
    # user_cart_list = user_cart_item.objects.filter(user_id=user_session_id)
    # for user_cart_row in user_cart_list:
    #     cart_det = user_cart_item.objects.filter(id=user_cart_row.id)
    #     cart_det.delete()


    return JsonResponse({'result':'1'})

def completation(request):
    context = home.common_data(request)
    return render(request, 'completation.html',context)

    
