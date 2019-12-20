from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    return render(request, 'home/home.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/sign_up.html')

