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
from debadmin.models import brand

def brand_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_brand = brand.objects.all().order_by('-id')
    context = {'all_brand':all_brand,'brand_active':'active'}
    return render(request, 'brand/brand_list_view.html',context)

def brand_add_view(request):
    context = {'brand_active':'active'}
    return render(request, 'brand/brand_add_view.html',context)

def brand_insert(request):
    admin_session_id = request.session['admin_session_id']
    brand_name = request.POST["brand_name"]
    brand_image = request.FILES["brand_image"] 
    brand_image= deb_utility.image_resize(brand_image,(130,80))
    brand_info = brand(        
                            brand_name=brand_name,
                            brand_image=brand_image, 
                            status='active',
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            
                            )
    brand_info.save()
    messages.success(request,'Brand Inserted Successfully!')
    return redirect(brand_list_view)

def brand_edit_view(request , brand_id):
    brand_det=brand.objects.filter(id=brand_id)
    context = {'brand_det':brand_det,'brand_active':'active'}
    return render(request, 'brand/brand_edit_view.html',context)

def brand_update(request):
	admin_session_id = request.session['admin_session_id']
	update_id = request.POST["update_id"]
	
	brand_name = request.POST["brand_name"]
	# brand_image = request.FILES["brand_image"] 
	old_image = request.POST["old_image"]

	brand_data = brand.objects.filter(id=update_id)[0]
	brand_data.brand_name = brand_name
	brand_data.modified_date = datetime.now().date()
	brand_data.modified_by = admin_session_id

	try:
		if request.FILES["brand_image"]:
			# print('old_image : ',old_image,settings.BASE_DIR)
			image_url = settings.BASE_DIR+old_image
			image_url = image_url.replace('/','\\')
			# print('base path:',image_url)
			os.remove(image_url)
			updated_brand_image= deb_utility.image_resize(request.FILES["brand_image"],(130,80))
			brand_data.brand_image = updated_brand_image
			brand_data.save(update_fields=['brand_name', 'brand_image','modified_date','modified_by'])
		else:
			brand_data.save(update_fields=['brand_name', 'modified_date','modified_by'])
	except Exception as e:
		brand_data.save(update_fields=['brand_name', 'modified_date','modified_by'])

	messages.success(request,'Brand Updated Successfully!')
	return redirect(brand_list_view)

def brand_status_change(request):
    status = request.POST['status']
    brand_id = request.POST.getlist('id[]')
    
    for brand_id in brand_id:
        brand_data = brand.objects.filter(id=brand_id)[0]
        brand_data.status = status
        brand_data.save(update_fields=['status'])

    return JsonResponse({'result': '1'})

def brand_delete(request , brand_id):
	brand_det=brand.objects.filter(id=brand_id)[0]
	brand_image_path = brand_det.brand_image.url
	# print('customer_image_path : ',customer_image_path)
	image_url = settings.BASE_DIR+brand_image_path
	image_url = image_url.replace('/','\\')
	# print('base path:',image_url)
	os.remove(image_url)
	brand_det.delete()
	messages.success(request,'Brand Deleted Successfully!')
	return redirect(brand_list_view)
