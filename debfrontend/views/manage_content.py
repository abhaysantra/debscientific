from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from . import home, manage_login, manage_profile
from debadmin.models import enquiry, valuableCustomer,video,about,gallery,contactUs,faq,video,valuableCustomer,policy,category,contactUs

def about_us(request):
    context = home.common_data(request)
    about_content = about.objects.all()
    context['about_content'] = about_content
    return render(request, 'footer_pages/about_us.html',context)

def gallery_view(request):
    context = home.common_data(request)
    gallery_det = gallery.objects.filter(status='active')
    context['gallery_det'] = gallery_det
    return render(request, 'footer_pages/gallery.html',context)

def contact_us_view(request):
    context = home.common_data(request)
    return render(request, 'footer_pages/contact_us.html',context)

def faq_view(request):
    context = home.common_data(request)
    faq_det = faq.objects.all()
    context['faq_det'] = faq_det
    return render(request, 'footer_pages/faq.html',context)

def return_policy_view(request):
    context = home.common_data(request)
    policy_det = policy.objects.all()
    context['policy_det'] = policy_det
    return render(request, 'footer_pages/return_policy.html',context)

def privacy_policy_view(request):
    context = home.common_data(request)
    policy_det = policy.objects.all()
    context['policy_det'] =policy_det
    return render(request, 'footer_pages/privacy_policy.html',context)

def terms_of_use_view(request):
    context = home.common_data(request)
    policy_det = policy.objects.all()
    context['policy_det'] = policy_det
    return render(request, 'footer_pages/terms_use.html',context)

def our_valuable_customer(request):
    context = home.common_data(request)
    valuable_cus_det = valuableCustomer.objects.filter(status='active')
    context['valuable_cus_det'] = valuable_cus_det
    return render(request, 'footer_pages/our_valuable_customer.html',context)

def video_list(request):
    context = home.common_data(request)
    video_det = video.objects.filter(status='active')
    context['video_det'] = video_det
    return render(request, 'footer_pages/video.html',context)

def enquery_form_submit(request):
    full_name = request.POST["enq_name"]
    email = request.POST["enq_email"] 
    phone_number = request.POST["enq_phone"]
    message = request.POST["enq_message"]
    created_date = datetime.now().date()
    enquery_info = enquiry(name=full_name, phone_number=phone_number, email=email, message=message, created_date = created_date)
    enquery_info.save()  
    return JsonResponse({'result': '1'})