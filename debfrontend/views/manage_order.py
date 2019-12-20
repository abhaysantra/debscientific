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
from debadmin.models import adminUser, adminEmail, order, order_invoice, order_details, order_address, user_address


def my_order(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    
    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)
    order_list = order.objects.filter(order_customer_id=user_session_id).order_by('-id')
    order_details_list = order_details.objects.raw('SELECT * FROM debadmin_order_details od JOIN debadmin_product p ON od.order_product_id = p.id WHERE od.customer_id = %s'%user_session_id)
    
    context = home.common_data(request)
    context['user_detail'] = user_detail
    context['order_list'] = order_list
    context['order_details_list'] = order_details_list
    return render(request, 'my_order.html',context) 


def order_details_view(request, order_id, uniqu_id):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)
    
    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)
    order_info = order.objects.filter(id=order_id)
    order_detail_info = order_details.objects.raw('SELECT * FROM debadmin_order_details od JOIN debadmin_product p ON od.order_product_id = p.id WHERE od.order_id = %s'%order_id)
    order_address_info = user_address.objects.raw('SELECT * FROM debadmin_user_address ua JOIN debadmin_order_address oa ON ua.id = oa.deli_address_id WHERE oa.order_id = %s'%order_id)
    order_invoice_info = order_invoice.objects.filter(order_id=order_id)
    total_invoice = 0
    # print('total invoice : ',total_invoice)
    if len(list(order_invoice_info)):
        total_invoice = len(list(order_invoice_info))

    context = home.common_data(request)
    context['user_detail'] = user_detail
    context['order_info'] = order_info
    context['order_detail_info'] = order_detail_info
    context['order_address_info'] = order_address_info
    context['order_invoice_info'] = order_invoice_info
    context['total_invoice'] = total_invoice
    
    return render(request, 'order_details.html',context) 


def cancel_single_order(request):
    order_det_id = request.POST['order_det_id']
    order_update_info = order_details.objects.filter(id=order_det_id)[0]
    order_id = order_update_info.order_id

    order_update_info.order_product_status = 'Cancelled'
    order_update_info.save(update_fields=['order_product_status'])

    total_order = order_details.objects.filter(order_id=order_id)
    total_order_status = order_details.objects.filter(order_id=order_id,order_product_status='Cancelled')

    if len(total_order) == len(total_order_status):
        main_order_info = order.objects.filter(id=order_id)[0]
        main_order_info.order_status = 'Cancelled'
        main_order_info.save(update_fields = ['order_status'])

    return JsonResponse({'result':'1'})

def cancel_reason_submit(request):
    order_det_id = request.POST['order_det_id']
    cancel_reason = request.POST['cancel_reason']
    order_update_info = order_details.objects.filter(id=order_det_id)[0]

    order_update_info.cancel_date = datetime.now().date()
    order_update_info.cancel_reason = cancel_reason
    order_update_info.save(update_fields=['cancel_reason','cancel_date'])

    return JsonResponse({'result':'1'})

def return_reason_submit(request):
    order_det_id = request.POST['order_det_id']
    return_reason = request.POST['return_reason']
    order_update_info = order_details.objects.filter(id=order_det_id)[0]

    order_update_info.return_date = datetime.now().date()
    order_update_info.return_reason = return_reason
    order_update_info.return_status = 'Waiting'
    order_update_info.save(update_fields=['return_reason','return_date','return_status'])

    return JsonResponse({'result':'1'})
