from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from django.core import mail
import json, requests
from random import randint
# from django.contrib.auth.models import User
from . import home, manage_profile, manage_cart
from debadmin.models import adminUser, adminEmail, user_cart_item, product, otp_service

def login(request):
    context = home.common_data(request)
    return render(request, 'login/login.html',context)

def register(request):
    context = home.common_data(request)
    return render(request, 'login/sign_up.html',context)

def forgot_password(request):
    context = home.common_data(request)
    return render(request, 'login/forgot_password.html',context)

def fetch_password_n_send(request):
    try:
        email = request.POST['login_email']
        # email = request.POST.get('login_email',False)
        user_obj = adminUser.objects.filter(login_email=email)
        if user_obj:
            result = 'Your password has been sent to ' + email + '.'
            send_email_for_forgot_password(user_obj[0])
        else:
            result = 'Please Provide correct email id. This does not exist!!'
        return JsonResponse({'result':result})
    except Exception as e:
        return JsonResponse({'result':str(e)})

# send mail of password for forgot_password:
def send_email_for_forgot_password(user_obj):
    subject = 'Forgot Password Email' #request.POST.get('subject', '')
    message = 'Your password : '+ user_obj.login_password#request.POST.get('message', '')
    from_email = settings.EMAIL_HOST_USER #request.POST.get('from_email', '')
    connection = mail.get_connection()
    connection.open()
    # Construct an email message that uses the connection
    email1 = mail.EmailMessage(subject,message,from_email,[user_obj.login_email],connection=connection)
    email1.send() # Send the email
    connection.close()

def check_otp_service(request):
    recved_otp = request.POST["otp"]
    phone_number = request.POST["phone_number"]
    print('.............otp : phone_number :',recved_otp,phone_number)
    otp_obj = otp_service.objects.filter(phone_number=phone_number)
    result='no'
    if otp_obj:
        db_otp = otp_obj[0].otp
        if db_otp == recved_otp.strip():
            result='yes'
    
    return JsonResponse({'result':result})

def resend_otp(request): 
    phone_number = request.POST["phone_number"]
    print('.......................phone_number: ',phone_number)
    otp_obj = otp_service.objects.filter(phone_number=phone_number)
    if otp_obj:
        created_time = otp_obj[0].created_at
        current_time = datetime.now()
        print('created_time :',created_time,' current_time : ',current_time)
        time_elapsed = (current_time - created_time).total_seconds()
        print('expiry time_elapsed : ',time_elapsed)
        if time_elapsed > 180:
            print('OTP has expired...Please generate new OTP and set Expiry time:')
            otp_obj[0].otp = generate_otp_n_send(request, phone_number)
            otp_obj[0].created_at = datetime.now()
            otp_obj[0].save(update_fields = ['otp','created_at'])
        else:
            print('Resending... old OTP')
            otp = otp_obj[0].otp
            response_data = send_otp(request, phone_number, otp)
    else:
        otp = generate_otp_n_send(request, phone_number)
        otp_service_info = otp_service(phone_number = phone_number,otp=otp,created_at=datetime.now())
        otp_service_info.save()
    return JsonResponse({'result': 'OTP has been resent :'})

# this function will receive both email and phone number and generate otp
# and send it to front-end
def validate_email_id(request): 
    login_email = request.POST["login_email"]
    phone_number = request.POST["phone_number"]
    print('.......................phone_number: ',phone_number)
    user_obj = adminUser.objects.filter(login_email=login_email)
    if len(user_obj) ==1 :
        result = 0
    else:
        result = 1

    #dummy code now need to generate otp and send it to this phone number and front-end
    otp_obj = otp_service.objects.filter(phone_number=phone_number)
    if otp_obj:
        created_time = otp_obj[0].created_at
        current_time = datetime.now()
        time_elapsed = (current_time - created_time).total_seconds()
        if time_elapsed > 180:
            print('OTP has expired...Please generate new OTP and set Expiry time:')
            otp_obj[0].otp = generate_otp_n_send(request, phone_number)
            otp_obj[0].created_at = datetime.now()
            otp_obj[0].save(update_fields = ['otp','created_at'])
        else:
            print('Resend old OTP')
            otp = otp_obj[0].otp
            send_otp(request,phone_number,otp)
    else:
        otp = generate_otp_n_send(request, phone_number)
        otp_service_info = otp_service(phone_number = phone_number,otp=otp,created_at=datetime.now())
        otp_service_info.save()
    return JsonResponse({'result': result})

def generate_otp_n_send(request, phone_number):
    otp = randint(000000, 999999)
    send_otp(request, phone_number, otp)
    return str(otp)

# source link
# http://www.nikhilshirsath.com/blog/post_detail/phone-number-verification-using-otp-in-django/
def send_otp(request,user_phone, otp):
    response_data = {}

    # commented out for testing
    # if request.method == "POST":
    #     api_key = '6bf4a67a-1caa-11ea-9fa5-0200cd936042'
    #     # url = "https://2factor.in/API/V1/6bf4a67a-1caa-11ea-9fa5-0200cd936042​/SMS/9563887730​/AUTOGEN"
    #     url = "https://2factor.in/API/V1/6bf4a67a-1caa-11ea-9fa5-0200cd936042/SMS/"+str(user_phone)+"/"+str(otp)
    #     # url = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/"+user_phone+"/AUTOGEN/OTPSEND"
    #     response = requests.request("GET", url)
    #     data = response.json()
    #     print('data............: ',data['Details'])
    #     response_data = {'Message':'Success'}
    # else:
    #     response_data = {'Message':'Failed'}
    # return JsonResponse(response_data)
    return response_data

def register_submit(request):
    full_name = request.POST["full_name"]
    phone_number = request.POST["phone_number"] 
    login_email = request.POST["login_email"]
    confirm_password = request.POST["confirm_password"]
    print('.....................received data....from sign up page:')
    print(full_name,phone_number,login_email,confirm_password)

    ###### validate otp
    url = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/"+phone_number+"/AUTOGEN/OTPSEND"
    response = requests.request("GET", url)
    data = response.json()
    print('response data : ',data)

    # register_info = adminUser(        
    #                         user_type_id='2',
    #                         full_name=full_name, 
    #                         login_password=confirm_password,
    #                         login_email=login_email,
    #                         phone_number=phone_number,
    #                         status='active',
    #                         created_date=datetime.now().date(),
    #                         )
    # register_info.save()

    messages.success(request,'Registered Successfully! Please Login!')
    return redirect(login)

def user_login_action(request):
    login_email = request.POST["login_email"]
    login_password = request.POST["login_password"] 
    # print(login_email,login_password)
    check_login = adminUser.objects.raw('SELECT * FROM debadmin_adminuser WHERE login_email=%s AND login_password=%s',[login_email,login_password])
    if len(check_login)==1:
        if check_login[0].user_type_id==2 and check_login[0].status=='active':
            request.session['user_session_id'] = check_login[0].id
            
            # Move session cart item to user cart item
            if 'deb_cart_item' in request.session:
                user_session_id = request.session['user_session_id']
                session_cart_list = request.session['deb_cart_item']
                # product_ids=tuple(session_cart_list.keys())

                keys = session_cart_list.keys()
                product_ids = []
                for key in keys:
                    product_ids.append(key.split('_')[0])
                product_ids = tuple(product_ids)
                # print('product_ids tuple: ',product_ids)

                if len(session_cart_list) > 1:
                    cart_list = product.objects.raw('SELECT * FROM debadmin_product WHERE id IN %s' % (product_ids,) )
                if len(session_cart_list) == 1:
                    cart_list = product.objects.raw('SELECT * FROM debadmin_product WHERE id = %s' %product_ids )
                if len(session_cart_list) == 0:
                    cart_list = []

                for key in keys:
                    product_id = key.split('_')[0].strip()
                    addon_id_list = key.split('_')[1]
                    product_obj = product.objects.filter(id=int(product_id))[0]

                    pro_mrp_price = product_obj.mrp_price
                    pro_discount = product_obj.discount
                    pro_sell_price = product_obj.sell_price
                    pro_qty = session_cart_list[str(key)]

                    #If product already exist in user cart then update qty
                    print('addon_id_list : ',addon_id_list,' pro_qty : ',pro_qty)
                    addon_id_list = json.dumps(addon_id_list)
                    print('after json dump addon_id_list :',addon_id_list)
                    cart_update_info = user_cart_item.objects.filter(user_id=user_session_id, addon_id_list=addon_id_list)
                    if cart_update_info:
                        previous_qty = cart_update_info[0].cart_item_qty
                        cart_update_info[0].cart_item_qty = previous_qty + pro_qty
                        cart_update_info[0].save(update_fields=['cart_item_qty'])
                    
                    else: 
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


                    # for cart_list_row in cart_list:
                    #     product_id = cart_list_row.id
                    #     pro_mrp_price = cart_list_row.mrp_price
                    #     pro_discount = cart_list_row.discount
                    #     pro_sell_price = cart_list_row.sell_price
                    #     pro_qty = session_cart_list[str(product_id)]

                    #     #If product already exist in user cart then update qty
                    #     cart_update_info = user_cart_item.objects.filter(user_id=user_session_id, cart_item_id=product_id)
                    #     if cart_update_info:
                    #         previous_qty = cart_update_info[0].cart_item_qty
                    #         cart_update_info[0].cart_item_qty = previous_qty + pro_qty
                    #         cart_update_info[0].save(update_fields=['cart_item_qty'])
                        
                    #     else: 
                    #         cart_info = user_cart_item(
                    #                             user_id=user_session_id,
                    #                             cart_item_id=product_id,
                    #                             cart_mrp_price=pro_mrp_price,
                    #                             cart_item_qty=pro_qty,
                    #                             cart_discount=pro_discount,
                    #                             cart_sell_price=pro_sell_price,
                    #                             )
                    #         cart_info.save()
                # delete deb_cart_item from session
                if 'deb_cart_item' in request.session:
                    request.session.pop('deb_cart_item', None)
                    # del request.session['deb_cart_item']
                return redirect(manage_cart.order_summary)
            else:
                return redirect(manage_profile.dashboard)

        else:
            messages.error(request,'username or password not correct')
            return redirect(login)
    else:
        messages.error(request,'username or password not correct')
        return redirect(login)

def user_logout(request):
    # del request.session['user_session_id']
    request.session.pop('user_session_id', None)

    if 'deb_cart_item' in request.session:
        del request.session['deb_cart_item']
    
        
    messages.info(request,'Successfully Logout!')
    
    return redirect(login)