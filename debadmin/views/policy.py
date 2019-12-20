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
from debadmin.models import policy

def policy_add(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    policy_objs = policy.objects.all()
    context = {'policy':policy_objs, 'policy_active':'active'}
    return render(request, 'policy/policy_add.html',context)

def policy_data_insertion(request):
    privacy_policy = request.POST['privacy_policy']
    return_policy = request.POST['return_policy']
    terms_of_use = request.POST['terms_of_use']
    update_id = request.POST['hidden_id']
    try:
        policy_data = policy.objects.filter(id=update_id)[0]
        policy_data.privacy_policy = privacy_policy
        policy_data.return_policy = return_policy
        policy_data.terms_of_use = terms_of_use
        policy_data.modified_date = datetime.now().date()
        policy_data.modified_by = request.session['admin_session_id']
        policy_data.status = 'active'
        policy_data.save(update_fields=['privacy_policy', 'return_policy','terms_of_use', 'status','modified_date', 'modified_by'])
    except Exception as e:
        print('Object Does not exist..')
        obj = policy(privacy_policy=privacy_policy, return_policy=return_policy, terms_of_use = terms_of_use,status = 'active', 
            created_date = datetime.now().date(),created_by = request.session['admin_session_id'])
        obj.save()
    
    messages.success(request,'Policy Data Updated Successfully!')
    return redirect(policy_add)