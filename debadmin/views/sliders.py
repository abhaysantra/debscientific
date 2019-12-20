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
from debadmin.models import slider

def slider_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_slider = slider.objects.all().order_by('-id')
    context = {'all_slider':all_slider,'slider_active':'active'}
    return render(request, 'slider/slider_view.html',context)

def slider_add_view(request):
    context = {'slider_active':'active'}
    return render(request, 'slider/slider_add_view.html',context)

def slider_insert(request):
    admin_session_id = request.session['admin_session_id']
    title1 = request.POST["title1"]
    title2 = request.POST["title2"] 
    link = request.POST["link"]
    slider_image = request.FILES["slider_image"]
    uploaded_slider_image= deb_utility.image_resize(slider_image,(1920,520))
    slider_info = slider(        
                            title_1=title1,
                            title_2=title2, 
                            image=uploaded_slider_image,
                            link=link,
                            status='active',
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            )
    slider_info.save()

    messages.success(request,'Slider Inserted Successfully!')
    return redirect(slider_view)

def slider_edit_view(request , slider_id):
    slider_det=slider.objects.filter(id=slider_id)
    context = {'slider_det':slider_det,'slider_active':'active'}
    return render(request, 'slider/slider_edit_view.html',context)

def slider_update(request):
    admin_session_id = request.session['admin_session_id']
    update_id = request.POST["update_id"]
    print("update id: ",update_id)
    title_1 = request.POST["title1"]
    title_2 = request.POST["title2"] 
    link = request.POST["link"]
    old_image = request.POST["old_image"]
    
    slider_data = slider.objects.filter(id=update_id)[0]
    slider_data.title_1 = title_1
    slider_data.title_2 = title_2
    slider_data.link = link
    slider_data.modified_date = datetime.now().date()
    slider_data.modified_by = admin_session_id

    try:
        if request.FILES["slider_image"]:
            slider_image = request.FILES["slider_image"]
            # print('old_image : ',old_image,settings.BASE_DIR)
            image_url = settings.BASE_DIR+old_image
            image_url = image_url.replace('/','\\')
            # print('base path:',image_url)
            os.remove(image_url)
            uploaded_slider_image= deb_utility.image_resize(slider_image,(1920,520))
            slider_data.image = uploaded_slider_image
            slider_data.save(update_fields=['title_1', 'title_2','link','image','modified_date','modified_by'])
        else:
            slider_data.save(update_fields=['title_1', 'title_2','link','modified_date','modified_by'])
    except Exception as e:
        slider_data.save(update_fields=['title_1', 'title_2','link','modified_date','modified_by'])
    

    messages.success(request,'Slider Updated Successfully!')
    return redirect(slider_view)

def slider_status_change(request):
    status = request.POST['status']
    slider_id = request.POST.getlist('id[]')
    
    for slider_id in slider_id:
        slider_data = slider.objects.filter(id=slider_id)[0]
        slider_data.status = status
        slider_data.save(update_fields=['status'])


    return JsonResponse({'result': '1'})




