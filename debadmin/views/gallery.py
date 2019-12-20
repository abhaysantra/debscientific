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
from debadmin.models import gallery

def gallery_listview(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)
    gallery_objs = gallery.objects.all()
    context = {'gallery_objs':gallery_objs, 'gallery_active':'active'}
    return render(request, 'gallery/gallery_view.html',context)

def gallery_add_view(request):
    context = {'gallery_active':'active'}
    return render(request, 'gallery/gallery_add_view.html',context)

def gallery_edit_view(request , gallery_id):
    gallery_det=gallery.objects.filter(id=gallery_id)
    context = {'gallery_det':gallery_det,'gallery_active':'active'}
    return render(request, 'gallery/gallery_edit_view.html',context)

def gallery_insert(request):
    admin_session_id = request.session['admin_session_id']

    gallery_image = request.FILES["gallery_image"]
    uploaded_gallery_image= deb_utility.image_resize(gallery_image,(600,600))
    gallery_info = gallery(        
                image=uploaded_gallery_image,
                status='active',
                created_date=datetime.now().date(),
                created_by=admin_session_id,
                modified_date=datetime.now().date(),
                modified_by=admin_session_id,
                )
    gallery_info.save()

    messages.success(request,'Gallery Photo Inserted Successfully!')
    return redirect(gallery_listview)

def gallery_status_change(request):
    status = request.POST['status']
    gallery_id = request.POST.getlist('id[]')
    
    for gallery_id in gallery_id:
        gallery_data = gallery.objects.filter(id=gallery_id)[0]
        gallery_data.status = status
        gallery_data.save(update_fields=['status'])


    return JsonResponse({'result': '1'})

def gallery_update(request):
    admin_session_id = request.session['admin_session_id']
    update_id = request.POST["update_id"]
    print("update id: ",update_id)
    old_image = request.POST["old_image"]
    
    gallery_data = gallery.objects.filter(id=update_id)[0]

    gallery_data.modified_date = datetime.now().date()
    gallery_data.modified_by = admin_session_id

    try:
        if request.FILES["gallery_image"]:
            gallery_image = request.FILES["gallery_image"]
            uploaded_gallery_image= deb_utility.image_resize(gallery_image,(600,600))
            gallery_data.image = uploaded_gallery_image
            # print('old_image : ',old_image,settings.BASE_DIR)
            image_url = settings.BASE_DIR + old_image
            image_url = image_url.replace('/','\\')
            # print('base path:',image_url)
            os.remove(image_url)
            
            gallery_data.save(update_fields=['image','modified_date','modified_by'])
        else:
            gallery_data.save(update_fields=['modified_date','modified_by'])

    except Exception as e:
        gallery_data.save(update_fields=['modified_date','modified_by'])
    
    messages.success(request,'Gallery Photo Updated Successfully!')
    # messages.success(request,msg)
    return redirect(gallery_listview)

def gallery_delete(request, gallery_id):
    print("gallery_id id: ",gallery_id)
    gallery_det=gallery.objects.filter(id=gallery_id)[0]

    try:
        image_url = settings.BASE_DIR + gallery_det.image.url
        image_url = image_url.replace('/','\\')
        print('base path:',image_url)
        # delete gallery image from directory
        os.remove(image_url)
        # delete from database
        gallery.objects.filter(id=gallery_id)[0].delete()
    except Exception as e:
        print('Exception occurs when trying to delete gallery image')
    messages.success(request,'Gallery Photo Deleted Successfully!')
    return redirect(gallery_listview)


