from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from django.db.models import Q
from django.db.models import Max, Min
from django.db import connection
from . import home, manage_login
from debadmin.models import adminUser, order_details, product_enquiry, product, product_image, product_download_image, category, review, sub_product


def product_list(request, cat_id, cat_slug):
    cat_det = category.objects.filter(id=cat_id)

    if cat_det[0].parent_category == 0:
        # print('inside..if :cat_id :',cat_id)
        product_list = product.objects.raw('SELECT * FROM debadmin_product p JOIN debadmin_category c ON p.category_id = c.id WHERE c.id=%s OR c.parent_category=%s'%(cat_id,cat_id)) 
        category_id_list = category.objects.filter(Q(parent_category=cat_id))
        # print('category_id_list : ',category_id_list)
        price_list = product.objects.filter(category_id__in=category_id_list,price_available='yes').aggregate(Max('sell_price'), Min('sell_price'))
    else:
        # print('inside..else :cat_id :',cat_id)
        product_list = product.objects.filter(category_id=cat_id)
        price_list = product.objects.filter(category_id=cat_id,price_available='yes').aggregate(Max('sell_price'), Min('sell_price'))
        
    
    total_product_list = len(list(product_list))
    # print('price_list : ',price_list)

    if total_product_list == 0:
        price_list = {'sell_price__max': 0.00, 'sell_price__min': 0.00}

    # We need parent category list to dispaly in the front-end
    parent_category_list = category.objects.filter(parent_category=0)
    context = home.common_data(request)
    context['product_list'] = product_list
    context['total_product_list'] = total_product_list
    # context['sell_price_min'] = sell_price_min
    context['cat_id'] = cat_id
    context['price_list'] = price_list

    context['parent_category_list'] = parent_category_list

    return render(request, 'product_list.html',context) 


def product_details(request, product_id, product_slug):
    product_details = product.objects.filter(id=product_id)
    pro_img_det = product_image.objects.filter(product_id=product_id)
    pro_down_det = product_download_image.objects.filter(product_id=product_id)
    sub_product_det = sub_product.objects.filter(product_id=product_id)
    related_products = product.objects.exclude(id=product_id)
    review_list = adminUser.objects.raw('SELECT * FROM debadmin_adminuser u JOIN debadmin_review r ON u.id = r.user_id WHERE r.product_id = %s ORDER BY r.id DESC'%product_id)
    total_review = len(list(review_list))

    context = home.common_data(request)
    context['product_details'] = product_details
    context['pro_img_det'] = pro_img_det
    context['pro_down_det'] = pro_down_det
    context['related_products'] = related_products
    context['review_list'] = review_list
    context['total_review'] = total_review
    context['sub_product_det'] = sub_product_det

    return render(request, 'product_details.html',context)


def review_submit(request):
    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        product_id = request.POST['product_id']
        message = request.POST['review']
        ratings = int(request.POST['ratings'])
        rem_rating = 5 - ratings

        check_product_buyer = order_details.objects.filter(customer_id=user_session_id, order_product_id=product_id)
        if check_product_buyer:
            pro_update_info = product.objects.filter(id=product_id)[0]
            prev_rate = pro_update_info.avg_rating
            
            if prev_rate == 0:
                avg_rating = ratings
            else:
                avg_rating = int((prev_rate + ratings)/2)
                
            remaining_rating = 5 - avg_rating
            pro_update_info.avg_rating = avg_rating
            pro_update_info.remaining_rating = remaining_rating
            pro_update_info.save(update_fields=['avg_rating','remaining_rating'])

            review_info = review(
                            user_id = user_session_id,
                            product_id = product_id,
                            rating = ratings,
                            message = message,
                            remaining_rating = rem_rating,
                            date = datetime.now().date()
                                )
            review_info.save()

            
            result = 1
        else:
            result = 2
    else:
        result = 0

    return JsonResponse({'result':result})

def product_enquiry_view(request, enquiry_product_id):
    context = home.common_data(request)
    context['enquiry_product_id'] = enquiry_product_id
    return render(request, 'product_enquiry_view.html', context)

def product_enquiry_submission(request):
    product_id = int(request.POST["hidden_pro_id"])
    full_name = request.POST["full_name"]
    email = request.POST["email"]
    phone_number = request.POST["phone_number"]
    web_address = request.POST["web_address"]
    message = request.POST["message"]

    product_enquiry_obj = product_enquiry(
                            product_id = product_id,
                            full_name = full_name,
                            email = email,
                            phone_number = phone_number,
                            web_address = web_address,
                            message = message,
                            date = datetime.now().date()
                            )
    product_enquiry_obj.save()
    messages.info(request,'Enquiry Submitted Successfully')
    return redirect(home.index)
    # return render(request, 'product_enquiry_view.html', {'enquiry_product_id': product_id})

## check this function
def get_addon_total_price(request):
    #there could be case based on loggedin user and visiting user
    # user_session_id = request.session['user_session_id']

    product_id = request.POST['product_id']
    sub_product_list = request.POST['sub_product_list']
    # sub_product_list = request.POST.getlist('sub_product_list[]')
    print('sub_product_list : ',sub_product_list)

    # for list of addon product
    # sub_product_det_list = sub_product.objects.filter(id__in=sub_product_list)
    # product_det = product.objects.filter(id=product_id)

    # total_addon_price = 0
    # for sub_product_obj in sub_product_det_list:  
    #     total_addon_price += sub_product_obj.sub_product_price

    # main_product_update_price = total_addon_price + product_det[0].sell_price
    # return JsonResponse({'result': total_addon_price})

    # for single addon product
    sub_product_det_list = sub_product.objects.filter(id=sub_product_list)
    product_det = product.objects.filter(id=product_id)
    print('sub_product_det_list[0].sub_product_price :',sub_product_det_list[0].sub_product_price)

    return JsonResponse({'result': sub_product_det_list[0].sub_product_price})