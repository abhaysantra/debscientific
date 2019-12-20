from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from . import accounts, deb_utility
from debadmin.models import valuableCustomer

def valuable_customer_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_valuable_customer = valuableCustomer.objects.all().order_by('-id')
    context = {'all_valuable_customer':all_valuable_customer,'valuable_customer_active':'active'}
    return render(request, 'valuable_customer/valuable_customer_view.html',context)

def valuable_customer_add_view(request):
    context = {'valuable_customer_active':'active'}
    return render(request, 'valuable_customer/valuable_customer_add_view.html',context)

def valuable_customer_insert(request):
    admin_session_id = request.session['admin_session_id']
    customer_name = request.POST["customer_name"]
    customer_image = request.FILES["customer_image"] 
    uploaded_customer_image= deb_utility.image_resize(customer_image,(100,100))
    valuable_customer_info = valuableCustomer(        
                            customer_name=customer_name,
                            customer_image=uploaded_customer_image, 
                            status='active',
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            
                            )
    valuable_customer_info.save()

    messages.success(request,'Valuable Customer Inserted Successfully!')
    return redirect(valuable_customer_view)

def valuable_customer_edit_view(request , valuable_customer_id):
    valuable_customer_det=valuableCustomer.objects.filter(id=valuable_customer_id)
    context = {'valuable_customer_det':valuable_customer_det,'valuable_customer_active':'active'}
    return render(request, 'valuable_customer/valuable_customer_edit_view.html',context)

def valuable_customer_update(request):
	admin_session_id = request.session['admin_session_id']
	update_id = request.POST["update_id"]
	
	customer_name = request.POST["customer_name"]
	old_image = request.POST["old_image"]
	valuable_customer_data = valuableCustomer.objects.filter(id=update_id)[0]
	valuable_customer_data.customer_name = customer_name
	valuable_customer_data.modified_date = datetime.now().date()
	valuable_customer_data.modified_by = admin_session_id

	try:
		if request.FILES["customer_image"]:
			image_url = settings.BASE_DIR+old_image
			image_url = image_url.replace('/','\\')
			print('base path:',image_url)
			os.remove(image_url)
			uploaded_customer_image= deb_utility.image_resize(request.FILES["customer_image"],(100,100))
			valuable_customer_data.customer_image = uploaded_customer_image
			valuable_customer_data.save(update_fields=['customer_name', 'customer_image','modified_date','modified_by'])
		else:
			valuable_customer_data.save(update_fields=['customer_name', 'modified_date','modified_by'])
	except Exception as e:
		valuable_customer_data.save(update_fields=['customer_name', 'modified_date','modified_by'])


	messages.success(request,'Valuable Customer Updated Successfully!')
	return redirect(valuable_customer_view)

def valuable_customer_status_change(request):
    status = request.POST['status']
    valuable_customer_id = request.POST.getlist('id[]')
    
    for valuable_customer_id in valuable_customer_id:
        valuable_customer_data = valuableCustomer.objects.filter(id=valuable_customer_id)[0]
        valuable_customer_data.status = status
        valuable_customer_data.save(update_fields=['status'])


    return JsonResponse({'result': '1'})

def valuable_customer_delete(request , valuable_customer_id):
	valuable_customer_det=valuableCustomer.objects.filter(id=valuable_customer_id)[0]
	customer_image_path = valuable_customer_det.customer_image.url
	print('customer_image_path : ',customer_image_path)
	image_url = settings.BASE_DIR+customer_image_path
	image_url = image_url.replace('/','\\')
	print('base path:',image_url)
	os.remove(image_url)
	valuable_customer_det.delete()
	messages.success(request,'Valuable Customer Deleted Successfully!')
	return redirect(valuable_customer_view)
