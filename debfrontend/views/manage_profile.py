from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from . import home, manage_login
from debadmin.models import adminUser, adminEmail, countries, cities, states

def dashboard(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)

    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)
    context = home.common_data(request)
    context['user_detail'] = user_detail
    return render(request, 'dashboard/dashboard.html',context)

def change_password(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)

    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)
    context = home.common_data(request)
    context['user_detail'] = user_detail
    return render(request, 'my_profile/change_password.html',context)

def change_password_submit(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)

    con_pass = request.POST["con_pass"]
    hidden_user_id = request.POST["hidden_user_id"]
    
    user_data = adminUser.objects.get_or_create(id=hidden_user_id)[0]
    user_data.login_password = con_pass
    user_data.save(update_fields=['login_password'])

    messages.info(request,'Password Successfully Updated!')

    return redirect(change_password)

def edit_profile(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)

    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)

    all_countries = countries.objects.all()
    all_states = states.objects.filter(country_id = user_detail[0].country)
    all_cities = cities.objects.filter(state_id = user_detail[0].state)

    context = home.common_data(request)
    context['user_detail'] = user_detail
    context['all_countries'] = all_countries
    context['all_states'] = all_states
    context['all_cities'] = all_cities
    return render(request, 'my_profile/edit_profile.html',context)

def user_profile_update(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    user_session_id = request.session['user_session_id']
    full_name = request.POST["full_name"]
    login_email = request.POST["login_email"]
    phone_number = request.POST["phone_number"]
    pin_code = request.POST["pin_code"]
    country = request.POST["country"]
    state = request.POST["state"]
    city = request.POST["city"]
    gst_no = request.POST["gst_no"]
    address = request.POST["address"]
    old_image = request.POST["old_image"]
    update_user_id = request.POST["update_user_id"]
    
    user_data = adminUser.objects.get_or_create(id=update_user_id)[0]
    user_data.full_name = full_name
    user_data.login_email = login_email
    user_data.phone_number = phone_number
    user_data.gst_no = gst_no
    user_data.address = address
    user_data.city = city
    user_data.state = state
    user_data.country = country
    user_data.pin_code = pin_code
    user_data.modified_by = user_session_id
    user_data.modified_date = datetime.now().date()

    try:
        if request.FILES["profile_image"]:
            profile_image = request.FILES["profile_image"]
            
            if old_image:
                image_url = settings.BASE_DIR+old_image
                image_url = image_url.replace('/','\\')
                os.remove(image_url)
            
            user_data.profile_image = profile_image
            user_data.save(update_fields=['full_name','profile_image','login_email','phone_number','gst_no','address','city','state','country','pin_code','modified_by','modified_date'])
        else:
            print('Image update not works')
            user_data.save(update_fields=['full_name','login_email','phone_number','gst_no','address','city','state','country','pin_code','modified_by','modified_date'])
    except Exception as e:
        user_data.save(update_fields=['full_name','login_email','phone_number','gst_no','address','city','state','country','pin_code','modified_by','modified_date'])
    

    messages.info(request,'Your Profile Successfully Updated!')

    return redirect(dashboard)