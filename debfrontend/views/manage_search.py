from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.db.models import Q
from django.db.models import Max, Min
from django.template import Context
from django.core import serializers
from . import home, manage_login
from debadmin.models import adminUser, product_enquiry, product, product_image, product_download_image, category, review


def product_search(request):
    try:
        search_name = request.POST['search_name']
    except Exception as e:
        print('Exception : ',e)
        search_name = ''
    print('search string :',search_name)
    found_product_list = []
   
    merged_product_list = product.objects.raw("SELECT * FROM debadmin_product p JOIN debadmin_category c ON p.category_id = c.id")
    # for search operation
    for merged_pro_obj in merged_product_list:
        if merged_pro_obj.category_name.find(search_name) >= 0:
            found_product_list.append(merged_pro_obj)

    if found_product_list:
        product_list = 	found_product_list
        # print('sub list')
    else:
        product_list = product.objects.filter(product_name__icontains=search_name)
        # print('Normal list')

        
    	
    total_product_list = len(list(product_list))
    context = home.common_data(request)
    context['product_list'] = product_list
    context['total_product_list'] = total_product_list
    context['search_text'] = search_name

    return render(request, 'product_list.html',context)


def autocomplete_product_name(request):
    auto_pro_list = []
    search_name = request.POST['request']
    product_list = product.objects.filter(product_name__icontains=search_name)

    for product_list_row in product_list:
        auto_pro_list.append(product_list_row.product_name)

    return JsonResponse({'result':auto_pro_list})


def get_filter_product_list(request):
    min_price = request.POST['min_price']
    max_price = request.POST['max_price']

    print(min_price,max_price)
    product_list_to_show = product.objects.all()
    product_id_list_to_show = [product.id for product in product_list_to_show]

    product_list_to_hide = product.objects.exclude(sell_price__gt=min_price,sell_price__lt=max_price)
    product_id_list_to_hide = [product.id for product in product_list_to_hide]

    # data = serializers.serialize('json', product_list)    
    return HttpResponse(json.dumps({'product_id_list_to_show': product_id_list_to_show, 'product_id_list_to_hide':product_id_list_to_hide}), content_type="application/json")

def filtered_product_list(request):
    try:
        min_price = str(request.POST['hid_min'])
        max_price = str(request.POST['hid_max'])
    except Exception as e:
        print('inside...........exception')
        print(e)
    product_list = product.objects.filter(sell_price__range=[min_price,max_price])
    total_product_list = len(product_list)
    print('product data: ',len(product_list),product_list)
    filtered_product_id_list = [product.id for product in product_list]
     
    total_product_list = len(list(product_list))
    # price_list = {'sell_price__max': 0.00, 'sell_price__min': 0.00}
    price_list = product.objects.filter(id__in=filtered_product_id_list,price_available='yes').aggregate(Max('sell_price'), Min('sell_price'))

    if total_product_list == 0:
        price_list = {'sell_price__max': 0.00, 'sell_price__min': 0.00}

    # We need parent category list to dispaly in the front-end
    parent_category_list = category.objects.filter(parent_category=0)
    context = home.common_data(request)
    context['product_list'] = product_list
    context['total_product_list'] = total_product_list
    context['price_list'] = price_list
    
    context['parent_category_list'] = parent_category_list

    return render(request, 'product_list.html',context) 
