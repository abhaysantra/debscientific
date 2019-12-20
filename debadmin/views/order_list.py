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
from debadmin.models import order, adminUser, order_invoice , order_details, order_address, billing_address, user_address, product_image, product

def order_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    # Join order and userAdmin table to have customer and order data together and recent order comes first
    order_list = order.objects.raw('SELECT * FROM debadmin_order o JOIN debadmin_adminUser a ON o.order_customer_id = a.id ORDER BY o.id DESC')
    total_order = len(list(order_list))
    context = {'order_list':order_list,'total_order':total_order,'order_list_active':'active'}
    return render(request, 'order_list/order_list_view.html',context)

def order_details_view(request, order_id):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    order_info = order.objects.filter(id=order_id)
    order_details_info = order_details.objects.filter(order_id=order_id)
    pro_image_info = product_image.objects.raw('SELECT * FROM debadmin_product_image GROUP BY product_id')
    pro_details_info = product.objects.all()
    bil_address_info = billing_address.objects.raw('SELECT * FROM debadmin_billing_address ba JOIN debadmin_order_address oa ON ba.id = oa.bill_address_id WHERE oa.order_id = %s'%order_id)
    deli_address_info = user_address.objects.raw('SELECT * FROM debadmin_user_address ua JOIN debadmin_order_address oa ON ua.id = oa.deli_address_id WHERE oa.order_id = %s'%order_id)
    order_invoice_info = order_invoice.objects.filter(order_id=order_id)
    total_invoice = 0
    
    if len(list(order_invoice_info)):
        total_invoice = len(list(order_invoice_info))

    print('total invoice : ',total_invoice)

    context = {
                'order_info':order_info,
                'order_details_info':order_details_info,
                'bil_address_info':bil_address_info,
                'deli_address_info':deli_address_info,
                'pro_image_info':pro_image_info,
                'pro_details_info':pro_details_info,
                'order_invoice_info':order_invoice_info,
                'total_invoice':total_invoice,
                'order_list_active':'active'
                }
    return render(request, 'order_list/order_details_view.html',context)


def change_order_status(request):
    status = request.POST['status']
    order_id = request.POST['order_id']

    order_data = order.objects.filter(id=order_id)[0]
    order_data.order_status = status
    order_data.save(update_fields=['order_status'])

    order_details_data = order_details.objects.filter(order_id=order_id)
    for order_details_row in order_details_data:
        order_details_id = order_details_row.id
        order_det_info = order_details.objects.filter(id=order_details_id)[0]
        order_det_info.order_product_status = status
        order_det_info.save(update_fields=['order_product_status'])

    messages.success(request,'Status Changed Successfully!')
    return JsonResponse({'result': '1'})


def change_order_details_status(request):
    status = request.POST['status']
    order_det_id = request.POST['order_det_id']

    order_details_data = order_details.objects.filter(id=order_det_id)[0]
    order_id = order_details_data.order_id
    order_details_data.order_product_status = status
    order_details_data.save(update_fields=['order_product_status'])

    if status == 'Delivered':
        order_details_data.deliver_date = datetime.now().date()
        order_details_data.save(update_fields=['deliver_date'])

    order_det_info1 = order_details.objects.filter(order_id=order_id,order_product_status=status)
    order_det_info2 = order_details.objects.filter(order_id=order_id)

    # print('order_det_info1 :',len(order_det_info1))
    # print('order_det_info2 :',len(order_det_info2))

    if len(order_det_info1) == len(order_det_info2):
        order_info = order.objects.filter(id=order_id)[0]
        order_info.order_status = status
        order_info.save(update_fields=['order_status'])

    messages.success(request,'Status Changed Successfully!')
    return JsonResponse({'result': '1'})


def change_return_status(request):
    status = 'Returned'
    return_status = request.POST['status']
    order_det_id = request.POST['order_det_id']

    order_details_data = order_details.objects.filter(id=order_det_id)[0]
    order_id = order_details_data.order_id

    if return_status == 'Accepted':
        order_details_data.return_status = return_status
        order_details_data.order_product_status = status
        order_details_data.save(update_fields=['order_product_status','return_status'])
    else:
        order_details_data.return_status = return_status
        order_details_data.save(update_fields=['return_status'])

    order_det_info1 = order_details.objects.filter(order_id=order_id,order_product_status=status)
    order_det_info2 = order_details.objects.filter(order_id=order_id)

    if len(order_det_info1) == len(order_det_info2):
        order_info = order.objects.filter(id=order_id)[0]
        order_info.order_status = status
        order_info.save(update_fields=['order_status'])

    messages.success(request,'Status Changed Successfully!')
    return JsonResponse({'result': '1'})



# Low Stock List module
def low_stock_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)
    
    # list all products which have available quantity less than 10
    low_stock_list = product.objects.filter(available_qty__lte=30)
    # to find product image
    all_product_image = product_image.objects.raw('SELECT * FROM debadmin_product_image GROUP BY product_id')

    context = {'low_stock_list':low_stock_list,'total_low_stock_product':low_stock_list.count(), 'all_product_image':all_product_image, 'low_stock_list_active':'active'}
    return render(request, 'order_list/low_stock_list_view.html',context)