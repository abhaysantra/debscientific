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
from debadmin.models import about

def about_us_add(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    about_us = about.objects.all()
    context = {'about_us':about_us, 'about_active':'active'}
    return render(request, 'about/about_us_add.html',context)

def about_us_data_insertion(request):
    title = request.POST['about_title']
    content = request.POST['about_content']
    update_id = request.POST['hidden_id']
    old_image = request.POST['hidden_about_img']

    about_data = about.objects.filter(id=update_id)[0]
    about_data.title = title
    about_data.content = content
    about_data.created_date = datetime.now().date()

    try:
        if request.FILES["about_image"]:
            about_image = request.FILES["about_image"]
            updated_about_image= deb_utility.image_resize(about_image,(540,293))
            about_data.image = updated_about_image
            image_url = settings.BASE_DIR+old_image
            image_url = image_url.replace('/','\\')
            os.remove(image_url)
            about_data.save(update_fields=['title', 'content','image','created_date'])
        else:
            about_data.save(update_fields=['title', 'content','created_date'])
    except Exception as e:
        about_data.save(update_fields=['title', 'content','created_date'])

    messages.success(request,'AboutUs Data Updated Successfully!')
    return redirect(about_us_add)