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
from debadmin.models import faq

def faq_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_faq = faq.objects.all().order_by('-id')
    context = {'all_faq':all_faq,'faq_active':'active'}
    return render(request, 'faq/faq_list_view.html',context)

def faq_add_view(request):
    context = {'faq_active':'active'}
    return render(request, 'faq/faq_add_view.html',context)

def faq_insert(request):
    admin_session_id = request.session['admin_session_id']
    question = request.POST["question"]
    answer = request.POST["answer"] 
    # faq_image = request.FILES["faq_image"]
    faq_info = faq(        
                            question=question,
                            answer=answer, 
                            status='active',
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            
                            )
    faq_info.save()

    messages.success(request,'FAQ Inserted Successfully!')
    return redirect(faq_list_view)

def faq_edit_view(request , faq_id):
	faq_det = faq.objects.filter(id=faq_id)
	context = {'faq_det':faq_det,'faq_active':'active'}
	return render(request, 'faq/faq_edit_view.html',context)

def faq_update(request):
	admin_session_id = request.session['admin_session_id']
	update_id = request.POST["update_id"]

	question = request.POST["question"]
	answer = request.POST["answer"]
	faq_data = faq.objects.filter(id=update_id)[0]
	faq_data.question = question
	faq_data.answer = answer
	faq_data.modified_date = datetime.now().date()
	faq_data.modified_by = admin_session_id
	faq_data.save(update_fields=['question', 'answer','modified_date','modified_by'])
	messages.success(request,'FAQ Updated Successfully!')
	return redirect(faq_list_view)

def faq_status_change(request):
	status = request.POST['status']
	faq_id = request.POST.getlist('id[]') 
	for faq_id in faq_id:
		faq_data = faq.objects.filter(id=faq_id)[0]
		faq_data.status = status
		faq_data.save(update_fields=['status'])

	return JsonResponse({'result': '1'})

def faq_delete(request , faq_id):
	faq_det=faq.objects.filter(id=faq_id)[0]
	faq_det.delete()
	messages.success(request,'FAQ Deleted Successfully!')
	return redirect(faq_list_view)
