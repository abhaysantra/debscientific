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
from debadmin.models import adminUser

def user_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    user_list = adminUser.objects.filter(user_type_id = 2).order_by('-id')
    
    context = {'user_list':user_list,'user_list_active':'active'}
    return render(request, 'user_list/user_list_view.html',context)

def user_delete(request , user_id):
	user_det=adminUser.objects.filter(id=user_id)[0]

	try:
		user_profile_image_path = user_det.profile_image.url
		user_profile_image_url = settings.BASE_DIR+user_profile_image_path
		user_profile_image_url = user_profile_image_url.replace('/','\\')
		os.remove(user_profile_image_url)
	except Exception as e:
		print('Unable to delete user profile image !!!')
		print('Exception : ', e)

	user_det.delete()
	messages.error(request,'User Profile Deleted Successfully!')
	return redirect(user_list_view)

def user_status_change(request):
    status = request.POST['status']
    user_id_list = request.POST.getlist('id[]')

    for user_id in user_id_list:
        user_data = adminUser.objects.filter(id=user_id)[0]
        user_data.status = status
        user_data.save(update_fields=['status'])

    return JsonResponse({'result': '1'})