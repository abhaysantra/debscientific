from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from . import home, manage_login
from debadmin.models import adminUser


def my_notification(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    
    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)

    context = home.common_data(request)
    context['user_detail'] = user_detail

    return render(request, 'notification.html',context) 

def my_wallet(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    
    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)

    context = home.common_data(request)
    context['user_detail'] = user_detail

    return render(request, 'wallet.html',context)