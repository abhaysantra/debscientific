from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from . import accounts
from debadmin.models import contactUs

def contact_us_add(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    contact_us = contactUs.objects.all()
    context = {'contact_us':contact_us, 'contact_active':'active'}
    return render(request, 'contact/contact_us_add.html',context)


def contact_us_data_insertion(request):
	if 'admin_session_id' not in request.session:
		return redirect(accounts.login)
	admin_session_id = request.session['admin_session_id']
    
	update_contact_id = request.POST['update_contact_id']
	address = request.POST['address']
	contact_number = request.POST['contact_number']
	land_line_number = request.POST['land_line_number']
	mail = request.POST['email']
	map_address = request.POST['map_address']
	footer_content = request.POST['footer_content']

	if update_contact_id:
		contact_data = contactUs.objects.filter(id=update_contact_id)[0]
		contact_data.address = address
		contact_data.contact_number = contact_number
		contact_data.land_line_number = land_line_number
		contact_data.mail = mail
		contact_data.map_address = map_address
		contact_data.footer_content = footer_content
		contact_data.created_date = datetime.now().date()
		contact_data.created_by = admin_session_id

		contact_data.save(update_fields=['address', 'contact_number','land_line_number','mail','map_address', 'footer_content', 'created_date', 'created_by'])

	else:
		obj = contactUs(address=address, contact_number = contact_number, land_line_number = land_line_number, mail = mail, 
		map_address = map_address, footer_content = footer_content, created_date = datetime.now().date(), created_by = admin_session_id)
		obj.save()

	messages.success(request,'ContactUs Data Updated Successfully!')
	return redirect(contact_us_add)