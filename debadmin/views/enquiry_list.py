from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import Context
from . import accounts
from debadmin.models import enquiry, product_enquiry, product

def enquiry_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    enquiry_list = enquiry.objects.all().order_by('-id')
    
    context = {'enquiry_list':enquiry_list,'enquiry_list_active':'active'}
    return render(request, 'enquiry_list/enquiry_list_view.html',context)

def enquiry_delete(request , enquiry_id):
    enquiry_det=enquiry.objects.filter(id=enquiry_id)[0]

    enquiry_det.delete()
    messages.error(request,'Enquiry Deleted Successfully!')
    return redirect(enquiry_list_view)

# this is for product enquiry
def enquiry_product_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    enquiry_list = product_enquiry.objects.all().order_by('-id')
    product_list = product.objects.all().order_by('-id')
    
    context = {'enquiry_list':enquiry_list,'product_list':product_list,'enquiry_product_list_active':'active'}
    return render(request, 'enquiry_list/enquiry_product_list_view.html',context)

def enquiry_product_delete(request , enquiry_id):
	enquiry_det=product_enquiry.objects.filter(id=enquiry_id)[0]

	enquiry_det.delete()
	messages.error(request,'Enquiry product Deleted Successfully!')
	return redirect(enquiry_product_list_view)
