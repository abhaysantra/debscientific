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
from debadmin.models import video

def video_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_video = video.objects.all().order_by('-id')
    context = {'all_video':all_video,'video_active':'active'}
    return render(request, 'video/video_view.html',context)

def video_add_view(request):
    context = {'video_active':'active'}
    return render(request, 'video/video_add_view.html',context)

def video_insert(request):
    admin_session_id = request.session['admin_session_id']
    link = request.POST["link"]
    # for embedding of youtube link
    link_version = link.split('/')[-1]
    link = "https://youtube.com/embed/" + link_version

    # video_image = request.FILES["video_image"]
    video_info = video(        
                    link=link,
                    status='active',
                    created_date=datetime.now().date(),
                    created_by=admin_session_id,
                    modified_date=datetime.now().date(),
                    modified_by=admin_session_id,
                    )
    video_info.save()

    messages.success(request,'Video Link Inserted Successfully!')
    return redirect(video_view)

def video_edit_view(request , video_id):
    video_det=video.objects.filter(id=video_id)
    context = {'video_det':video_det,'video_active':'active'}
    return render(request, 'video/video_edit_view.html',context)

def video_update(request):
    admin_session_id = request.session['admin_session_id']
    update_id = request.POST["update_id"]
    link = request.POST["link"]
    # for embedding of youtube link
    link_version = link.split('/')[-1]
    link = "https://youtube.com/embed/" + link_version

    video_data = video.objects.filter(id=update_id)[0]
    video_data.link = link
    video_data.modified_date = datetime.now().date()
    video_data.modified_by = admin_session_id

    print("update id: ",update_id,link)
    video_data.save(update_fields=['link','modified_date','modified_by'])
    messages.success(request,'Video Link Updated Successfully!')
    return redirect(video_view)

def video_status_change(request):
    status = request.POST['status']
    video_id = request.POST.getlist('id[]')
    
    for video_id in video_id:
        video_data = video.objects.filter(id=video_id)[0]
        video_data.status = status
        video_data.save(update_fields=['status'])


    return JsonResponse({'result': '1'})

def video_delete(request , video_id):
	video_det=video.objects.filter(id=video_id)[0]
	video_det.delete()
	messages.success(request,'Video Link Deleted Successfully!')
	return redirect(video_view)
