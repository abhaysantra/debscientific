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
from debadmin.models import banner

def banner_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    banner_list = banner.objects.all()
    context = {'banner_list':banner_list, 'banner_active':'active'}
    return render(request, 'banner/banner_view.html',context)

def banner_add_view(request):
    context = {'banner_active':'active', 'banner_active':'active'}
    return render(request, 'banner/banner_add_view.html',context)

def banner_insert(request):
    title_1 = request.POST['title_1']
    title_2 = request.POST['title_2']
    link = request.POST['link']
    banner_type = request.POST['banner_type']
    # old_image = request.POST['hidden_about_img']

    banner_image = request.FILES["banner_image"]
    if banner_type == 'first_row':
        size = (550,221)
    else:
        size = (1920,370)
    uploaded_banner_image= deb_utility.image_resize(banner_image,size)
    banner_info = banner(        
                    title_1=title_1,
                    title_2=title_2, 
                    banner_image=uploaded_banner_image,
                    link=link,
                    banner_type = banner_type,
                    created_date=datetime.now().date(),
                    )
    banner_info.save()

    messages.success(request,'Banner Data Updated Successfully!')
    return redirect(banner_view)

def banner_edit_view(request , banner_id):
    banner_det=banner.objects.filter(id=banner_id)
    context = {'banner_det':banner_det, 'banner_active':'active'}
    return render(request, 'banner/banner_edit_view.html',context)

def banner_update(request):
    admin_session_id = request.session['admin_session_id']
    update_id = request.POST["update_id"]
    print("update id: ",update_id)
    title_1 = request.POST["title_1"]
    title_2 = request.POST["title_2"] 
    #when banner type 'first row' then title_3 not present
    try:
        title_3 = request.POST["title_3"]
    except:
        title_3 = None
    link = request.POST["link"]
    old_image = request.POST["old_image"]
    banner_type = request.POST['banner_type']
    if banner_type == 'first_row':
        size = (550,221)
    else:
        size = (1920,370)
    
    banner_data = banner.objects.filter(id=update_id)[0]
    banner_data.title_1 = title_1
    banner_data.title_2 = title_2
    banner_data.title_3 = title_3
    banner_data.link = link
    banner_data.modified_date = datetime.now().date()

    try:
        if request.FILES["banner_image"]:
            banner_image = request.FILES["banner_image"]
            uploaded_banner_image= deb_utility.image_resize(banner_image,size)
            # print('old_image : ',old_image,settings.BASE_DIR)
            image_url = settings.BASE_DIR+old_image
            image_url = image_url.replace('/','\\')
            # print('base path:',image_url)
            os.remove(image_url)
            banner_data.banner_image = uploaded_banner_image
            banner_data.save(update_fields=['title_1', 'title_2','title_3','link','banner_image','modified_date'])
        else:
            banner_data.save(update_fields=['title_1', 'title_2','title_3','link','modified_date'])
    except Exception as e:
        banner_data.save(update_fields=['title_1', 'title_2','title_3','link','modified_date'])
    

    messages.success(request,'Banner Updated Successfully!')
    return redirect(banner_view)