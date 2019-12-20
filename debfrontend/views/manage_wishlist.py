from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import home,manage_login
from debadmin.models import user_wish_list, adminUser

def add_to_wishlist(request):
    product_id = request.POST['product_id']

    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        wishlist_info = user_wish_list(
                                    user_id = user_session_id,
                                    product_id = product_id,
                                        )
        wishlist_info.save()
        result = 1

    else:
        result = 0
        
    return JsonResponse({'result': result})


def wishlist(request):
    context = home.common_data(request)
    # print('context data: ',context)
    return render(request, 'wishlist.html',context)

def my_wishlist(request):
    if 'user_session_id' not in request.session:
        return redirect(manage_login.login)

    user_session_id = request.session['user_session_id']
    user_detail = adminUser.objects.filter(id=user_session_id)
    context = home.common_data(request)
    context['user_detail'] = user_detail
    return render(request, 'wishlist_dashboard.html',context)


def remove_from_wishlist(request):
    product_id = request.POST['product_id']

    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        user_wish_list.objects.filter(product_id=product_id, user_id=user_session_id)[0].delete()
        result = 1
    else:
        result = 0
        
    return JsonResponse({'result': result})


def remove_wishlist_after_cart(request):
    product_id = request.POST['product_id']

    if 'user_session_id' in request.session:
        user_session_id = request.session['user_session_id']
        user_wish_list.objects.filter(product_id=product_id, user_id=user_session_id)[0].delete()
        result = 1
    else:
        result = 0
        
    return JsonResponse({'result': product_id})


