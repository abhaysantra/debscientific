from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from django.core import serializers
from collections import OrderedDict 
from django.db.models import Q
from . import accounts
from debadmin.models import adminUser, adminEmail, category

def category_listview(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_category = category.objects.all().order_by('-id')
    # finding parent category name
    parent_category_list = category.objects.filter(parent_category = 0)
    sub_category_list = category.objects.filter(~Q(parent_category = 0),Q(sub_category = 0))
    context = {'all_category':all_category,'sub_category_list':sub_category_list,'category_active':'active', 'parent_category_list': parent_category_list}
    print('sub_category_list : ',sub_category_list)
    return render(request, 'category/category_table.html',context)

def category_add_view(request):
    parent_cat_list = category.objects.filter(parent_category=0)
    context = {'category_active':'active','parent_cat_list':parent_cat_list}
    return render(request, 'category/category_add_view.html',context)

def category_insert(request):
    admin_session_id = request.session['admin_session_id']
    parent_category = request.POST["parent_cat"]
    sub_category = request.POST["sub_category"]
    category_name = request.POST["cat_name"]
    category_slug = request.POST["cat_slug"]
    description = request.POST["cat_desc"]
    category_status = request.POST["status"]
    category_meta_title = request.POST["meta_tag"]
    category_meta_description = request.POST["meta_desc"]
    category_meta_keyword = request.POST["meta_key"]
    
    # if parent category not provided then it is parent category
    if parent_category:
        category_info = category(        
                            parent_category=parent_category,
                            sub_category = sub_category,
                            category_name=category_name,
                            category_slug=category_slug, 
                            description=description,
                            category_status=category_status,
                            category_meta_title=category_meta_title,
                            category_meta_description=category_meta_description,
                            category_meta_keyword=category_meta_keyword,
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            )
        category_info.save()
    else:
        category_info = category(        
                            parent_category='0',
                            sub_category = '0',
                            category_name=category_name,
                            category_slug=category_slug, 
                            description=description,
                            category_status=category_status,
                            category_meta_title=category_meta_title,
                            category_meta_description=category_meta_description,
                            category_meta_keyword=category_meta_keyword,
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            )
        category_info.save()

    messages.success(request,'Category Inserted Successfully!')
    return redirect(category_listview)

def category_edit_view(request , category_id):
    parent_cat_list = category.objects.filter(parent_category=0)
    category_det=category.objects.filter(id=category_id)
    selected_parent_cat = category_det[0].parent_category
    sub_category_list = category.objects.filter(parent_category = selected_parent_cat, sub_category = 0)
    context = {'sub_category_list':sub_category_list, 'category_det':category_det,'parent_cat_list':parent_cat_list,'category_active':'active'}
    return render(request, 'category/category_edit_view.html',context)

def category_update(request):
    admin_session_id = request.session['admin_session_id']
    update_id = request.POST["cat_edit_id"]
   
    parent_category = request.POST["parent_cat"]
    sub_category = request.POST["sub_category"]
    category_name = request.POST["cat_name"]
    category_slug = request.POST["cat_slug"]
    description = request.POST["cat_desc"]
    category_status = request.POST["status"]
    category_meta_title = request.POST["meta_tag"]
    category_meta_description = request.POST["meta_desc"]
    category_meta_keyword = request.POST["meta_key"]
    
    category_data = category.objects.filter(id=update_id)[0]

    category_data.parent_category = parent_category
    category_data.sub_category = sub_category
    category_data.category_name = category_name
    category_data.category_slug = category_slug
    category_data.description = description
    category_data.category_status = category_status
    category_data.category_meta_title = category_meta_title
    category_data.category_meta_description = category_meta_description
    category_data.category_meta_keyword = category_meta_keyword
    category_data.modified_date = datetime.now().date()
    category_data.modified_by = admin_session_id

    category_data.save(update_fields=[
                                    'parent_category',
                                    'sub_category',
                                    'category_name',
                                    'category_slug',
                                    'description',
                                    'category_status',
                                    'category_meta_title',
                                    'category_meta_description',
                                    'category_meta_keyword',
                                    'modified_date',
                                    'modified_by']
                                    )

    messages.success(request,'Category Updated Successfully!')
    return redirect(category_listview)

def category_delete(request , category_id):
	category_det=category.objects.filter(id=category_id)[0]
	category_det.delete()
	messages.success(request,'Category Deleted Successfully!')
	return redirect(category_listview)

def category_status_change(request):
    category_status = request.POST['status']
    category_id = request.POST.getlist('id[]')
    
    for category_id in category_id:
        category_data = category.objects.filter(id=category_id)[0]
        category_data.category_status = category_status
        category_data.save(update_fields=['category_status'])

    return JsonResponse({'result': '1'})

def get_subcategory(request):
    parent_cat = request.POST['parent_cat']
    response_data_dict = {}

    category_data_list = category.objects.filter(parent_category=parent_cat, sub_category = 0)
    for cat_obj in category_data_list:        
        response_data_dict[str(cat_obj.id)] = cat_obj.category_name

    return JsonResponse(response_data_dict)

