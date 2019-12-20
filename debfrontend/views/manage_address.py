from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from . import home, manage_login, manage_profile
from debadmin.models import adminUser, user_address, countries, cities, states


def my_address_list(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    
    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)

    user_address_detail_list = user_address.objects.filter(user_id=user_session_id)
    context = home.common_data(request)
    context['user_detail'] = user_detail
    context['user_address_detail_list'] = user_address_detail_list
    return render(request, 'manage_address.html',context)

def add_new_address(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    
    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)

    ##########testing with countries data
    # python manage.py makemigrations debadmin --fake :: to remove migration error after deletion of countries table
    all_countries = countries.objects.all()
    # all_states = states.objects.all()
    # all_cities = cities.objects.all()

    context = home.common_data(request)
    context['user_detail'] = user_detail

    context['all_countries'] = all_countries

    return render(request, 'add_address.html',context)

def get_state_list(request):
	country_id = request.POST['country_id']
	state_obj_list = states.objects.filter(country_id=country_id)
	state_dict = {}
	for state in state_obj_list:
		state_dict[str(state.state_id)] = state.name
	return JsonResponse(state_dict)

def get_city_list(request):
	state_id = request.POST['state_id']
	cities_obj_list = cities.objects.filter(state_id=state_id)
	city_dict = {}
	for city in cities_obj_list:
		city_dict[str(city.city_id)] = city.name
	# print('city_dict : ',city_dict)
	return JsonResponse(city_dict)

def get_country_state_city_name(request):
	country_id = request.POST['country_id']
	state_id = request.POST['state_id']
	city_id = request.POST['city_id']
	country_obj = countries.objects.filter(country_id=country_id)[0]
	states_obj = states.objects.filter(state_id=state_id)[0]
	cities_obj = cities.objects.filter(city_id=city_id)[0]
	data_dict = {}
	data_dict['country'] = country_obj.name
	data_dict['state'] = states_obj.name
	data_dict['city'] = cities_obj.name
	# print('data_dict : ',data_dict)
	return JsonResponse(data_dict)

def insert_new_address(request):
	if 'user_session_id' not in request.session:
		return redirect(manage_login.login)

	user_session_id = request.session['user_session_id']
	full_name = request.POST["full_name"]
	email = request.POST["email"]
	ph_no = request.POST["ph_no"]
	alt_phone_no = request.POST["alt_phone_no"]

	pin_code = request.POST["pin_code"]
	country = request.POST["country"]
	state = request.POST["state"]
	city = request.POST["city"]
	landmark = request.POST["landmark"]

	gst_no = request.POST["gst_no"]
	address = request.POST["address"]
	post_office = request.POST["post_office"]
	address_type = request.POST["address_type"]

	user_address_info = user_address(
							user_id = user_session_id,
							full_name = full_name,
							email = email,
							mobile_number = ph_no,
							alt_mobile_number = alt_phone_no,
							pincode = pin_code,
							country = country,
							state = state,
							city = city,
							landmark = landmark,
							gst_no = gst_no,
							address = address,
							address_type = address_type,

							post_office = post_office,
							created_date = datetime.now().date(),
							created_by = user_session_id

							)
	user_address_info.save()
	messages.info(request,'Address Added Successfully')
	return redirect(my_address_list)

def change_address_status(request):
	user_address_id = request.POST['address_id']

	user_session_id = request.session['user_session_id']
	user_address_detail_obj_list = user_address.objects.filter(user_id=user_session_id)
	for user_address_detail_obj in user_address_detail_obj_list:
		user_address_detail_obj.is_default = 'no'
		if str(user_address_detail_obj.id).strip() == str(user_address_id).strip():
			user_address_detail_obj.is_default = 'yes'

		user_address_detail_obj.modified_date = datetime.now().date()
		user_address_detail_obj.modified_by = user_session_id
		user_address_detail_obj.save(update_fields=['is_default', 'modified_date', 'modified_by'])
	messages.info(request,'Address Status Changed Successfully')
	return JsonResponse({'result': '1'})

def user_address_delete(request):
	user_address_id = request.POST['address_id']
	user_address_detail_obj_list = user_address.objects.filter(id=user_address_id).delete()
	
	messages.info(request,'User Address Deleted Successfully')
	return JsonResponse({'result': '1'})

def user_address_edit_view(request, user_address_id):
	if 'user_session_id' not in request.session:
		return redirect(manage_login.login)

	user_session_id = request.session['user_session_id']

	#todo check if user does not enter any address during registration
	user_address_detail = user_address.objects.filter(id=user_address_id)[0]
	user_detail = adminUser.objects.filter(id=user_session_id)
	all_countries = countries.objects.all()
	all_states = states.objects.filter(country_id = user_address_detail.country)
	all_cities = cities.objects.filter(state_id = user_address_detail.state)

	context = home.common_data(request)
	context['user_detail'] = user_detail
	context['user_address_detail'] = user_address_detail
	context['all_countries'] = all_countries
	context['all_states'] = all_states
	context['all_cities'] = all_cities

	return render(request, 'user_address_edit.html',context)

def user_address_update(request, user_address_id):
	if 'user_session_id' not in request.session:
		return redirect(manage_login.login)

	user_session_id = request.session['user_session_id']
	full_name = request.POST["full_name"]
	email = request.POST["email"]
	ph_no = request.POST["ph_no"]
	alt_phone_no = request.POST["alt_phone_no"]

	pin_code = request.POST["pin_code"]
	country = request.POST["country"]
	state = request.POST["state"]
	city = request.POST["city"]
	landmark = request.POST["landmark"]

	gst_no = request.POST["gst_no"]
	address = request.POST["address"]
	post_office = request.POST["post_office"]
	address_type = request.POST["address_type"]

	user_address_detail_obj = user_address.objects.filter(id=user_address_id)[0]
	user_address_detail_obj.modified_date = datetime.now().date()
	user_address_detail_obj.modified_by = user_session_id

	user_address_detail_obj.full_name = full_name
	user_address_detail_obj.email = email
	user_address_detail_obj.mobile_number = ph_no
	user_address_detail_obj.alt_mobile_number = alt_phone_no
	user_address_detail_obj.pincode = pin_code
	user_address_detail_obj.country = country
	user_address_detail_obj.state = state
	user_address_detail_obj.city = city
	user_address_detail_obj.landmark = landmark
	user_address_detail_obj.gst_no = gst_no
	user_address_detail_obj.address = address
	user_address_detail_obj.post_office = post_office
	user_address_detail_obj.address_type = address_type

	user_address_detail_obj.save(update_fields=['full_name','email','mobile_number','alt_mobile_number','pincode','country','state','city','landmark','gst_no','address','post_office','address_type', 'modified_date', 'modified_by'])
	messages.info(request,'Address Update Successfully')

	return redirect(my_address_list)


    
