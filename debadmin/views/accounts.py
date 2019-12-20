from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from debadmin.models import adminUser, adminEmail, enquiry, product, category, brand, order

def login(request):
    return render(request, 'login.html')

def login_action(request):
    login_email = request.POST["login_email"]
    login_password = request.POST["login_password"] 
    # print(login_email,login_password)
    check_login = adminUser.objects.raw('SELECT * FROM debadmin_adminuser WHERE login_email=%s AND login_password=%s',[login_email,login_password])
    if len(check_login)==1:
        if check_login[0].user_type_id==1:
            request.session['admin_session_id'] = check_login[0].id
            request.session['admin_session_name'] = check_login[0].full_name
            return redirect(index)
        else:
            messages.error(request,'username or password not correct')
            return redirect(login)
    else:
        messages.error(request,'username or password not correct')
        return redirect(login)  

def logout(request):
    del request.session['admin_session_id']
    del request.session['admin_session_name']
    messages.info(request,'Successfully Logout!')
    
    return redirect(login)

def index(request):
    if 'admin_session_id' not in request.session:
        return redirect(login)
    else:
        all_product = product.objects.all()
        all_category = category.objects.all()
        all_enquiry = enquiry.objects.all()
        all_users = adminUser.objects.filter(user_type_id = 2).order_by('-id')
        all_brands = brand.objects.all()
        all_orders = order.objects.all()
        context = {
            'all_product':all_product,
            'all_category':all_category,
            'all_enquiry':all_enquiry,
            'all_users':all_users,
            'all_brands':all_brands,
            'all_orders':all_orders
        }
        return render(request, 'dashboard_view.html', context)
   
def admin_profile(request):
    if 'admin_session_id' not in request.session:
        return redirect(login)

    admin_session_id = request.session['admin_session_id']
    profile_data = adminUser.objects.get_or_create(id=admin_session_id)
   
    return render(request, 'admin_profile_edit.html', {'profile_data':profile_data})

def admin_profile_edit(request):
    full_name = request.POST["full_name"]
    email = request.POST["email"]
    userid = request.POST["userid"]

    profile_data = adminUser.objects.get_or_create(id=userid)[0]
    profile_data.full_name = full_name
    profile_data.login_email = email
    profile_data.save(update_fields=['full_name', 'login_email'])

    messages.info(request,'Profile Successfully Updated!')

    return redirect(admin_profile)

def admin_password_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(login)

    admin_session_id = request.session['admin_session_id']
    profile_data = adminUser.objects.get_or_create(id=admin_session_id)
   
    return render(request, 'admin_password_change.html', {'profile_data':profile_data})

def admin_password_update(request):
    if 'admin_session_id' not in request.session:
        return redirect(login)

    con_pass = request.POST["con_pass"]
    hidden_user_id = request.POST["hidden_user_id"]
    
    adminObj = adminUser.objects.get_or_create(id=hidden_user_id)[0]
    adminObj.login_password = con_pass
    adminObj.save(update_fields=['login_password'])

    messages.info(request,'Password Successfully Updated!')

    return redirect(admin_password_view)

def admin_email_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(login)

    admin_session_id = request.session['admin_session_id']
    email_data = adminEmail.objects.get_or_create(id=1)
   
    return render(request, 'admin_email_view.html', {'email_data':email_data})

def admin_email_update(request):
    if 'admin_session_id' not in request.session:
        return redirect(login)

    receive_email = request.POST["receive_email"]
    from_email = request.POST["from_email"]
    
    email_data = adminEmail.objects.get_or_create(id=1)[0]
    email_data.receive_email = receive_email
    email_data.from_email = from_email
    email_data.save(update_fields=['receive_email', 'from_email'])

    messages.info(request,'Email Successfully Updated!')

    return redirect(admin_email_view)