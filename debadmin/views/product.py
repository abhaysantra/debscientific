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
from PIL import Image
from . import accounts, deb_utility
from debadmin.models import brand, product, sub_product, category, product_image, product_download_image, review

def product_list_view(request):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_product = product.objects.all().order_by('-id')
    all_category = category.objects.all().order_by('-id')
    parent_category_list = category.objects.filter(parent_category = 0)
    sub_category_list = category.objects.filter(~Q(parent_category = 0),Q(sub_category = 0))
    # print('sub_category_list : ',sub_category_list)
    all_product_image = product_image.objects.raw('SELECT * FROM debadmin_product_image GROUP BY product_id')

    context = {'all_product':all_product,'all_product_image':all_product_image,'all_category':all_category, 'parent_category_list': parent_category_list,'sub_category_list':sub_category_list, 'product_active':'active'}
    return render(request, 'product/product_view.html',context)

def product_add_view(request):
    all_category = category.objects.all().order_by('-id')
    all_brand = brand.objects.all().order_by('-id')
    # finding parent category name
    parent_category_list = category.objects.filter(parent_category = 0)
    sub_category_list = category.objects.filter(~Q(parent_category = 0),Q(sub_category = 0))
    # print('sub_category_list : ',sub_category_list)
    context = {'all_category':all_category, 'parent_category_list': parent_category_list, 'all_brand': all_brand,'sub_category_list':sub_category_list, 'product_active':'active'}
    return render(request, 'product/product_add_view.html',context)


def product_insert(request):
    admin_session_id = request.session['admin_session_id']

    category_id = request.POST["category_id"]
    brand_id = request.POST["brand_id"]
    product_name = request.POST["product_name"]
    product_slug = request.POST["product_slug"]
    price_available = request.POST["price_available"]
    gst = request.POST["gst"]
    if gst == '':
        gst = 0.0
    mrp_price = request.POST["mrp_price"]
    sale_price = request.POST["sale_price"]
    discount = request.POST["discount"]
    if price_available == 'no':
        mrp_price = sale_price = discount = 0.0
    qty = request.POST["qty"]
    if qty == '':
        qty = 0
    product_description = request.POST["product_description"]
    product_specification = request.POST["product_specification"]

    ################
    product_weight = request.POST["product_weight"]
    product_weight_class = request.POST["product_weight_class"]
    # properties = request.POST["properties"]
    ################
    shipping_product_length = request.POST["shipping_product_length"]
    shipping_product_width = request.POST["shipping_product_width"]
    shipping_product_height = request.POST["shipping_product_height"]
    shipping_dimension_class = request.POST["shipping_dimension_class"]
    meta_title = request.POST["meta_title"]
    meta_key = request.POST["meta_key"]
    meta_description = request.POST["meta_description"]
    pro_images = request.FILES.getlist("product_image[]")  #image array lis
    download_images = request.FILES.getlist("download_image[]")    # Download image array list

    product_info = product(        
                            category_id=category_id,
                            brand_id=brand_id, 
                            product_name=product_name, 
                            product_slug=product_slug, 
                            product_desc=product_description,
                            product_specification = product_specification, 
                            product_weight=product_weight, 
                            product_weight_class=product_weight_class,  
                            available_qty=qty,
                            price_available = price_available,
                            gst = gst, 
                            mrp_price=mrp_price, 
                            discount=discount, 
                            sell_price=sale_price,  
                            product_status='active',
                            shipping_product_length=shipping_product_length,
                            shipping_product_width=shipping_product_width,
                            shipping_product_height=shipping_product_height,
                            shipping_dimension_class=shipping_dimension_class,
                            meta_title=meta_title, 
                            meta_keyword=meta_key, 
                            meta_description=meta_description,
                            created_date=datetime.now().date(),
                            created_by=admin_session_id,
                            )
    product_info.save()

    product_id = product_info.id  #Get Insert Product Id
    # print('Insert Product Id: ',product_id)

    for pro_image in pro_images:
        print('pro_image : ',pro_image)
        if str(pro_image).find('.pdf')>= 0:
            image_list = pro_image
            image_detail = pro_image
            product_image_info = product_image(
                                        product_id=product_id,
                                        product_list=image_list,
                                        product_details=image_detail,
                                        created_date=datetime.now().date(),
                                        )
            # product_image_info.save()
            print('product_image_info : url: ',product_image_info.product_list)
            product_image_path = os.path.join(settings.BASE_DIR,'media','product_list')
            product_image_path = product_image_path.replace('/','\\')
            # os.remove(product_image_path)
            print('product_image_path : ',product_image_path)
            print('product_image_info.product_list : ',product_image_info.product_list)
            # image_name = str(product_image_info.product_list).split('/')[1]
            image_name = product_image_info.product_list
            # path = product_image_path + '/'+product_image_info.product_list
            # print('path : ',path)
            image_list= deb_utility.convert_pdf_2_image(product_image_path,image_name,(229,188))
            # image_detail= deb_utility.image_resize(product_image_path,(600,600))

        else:
            image_list= deb_utility.image_resize(pro_image,(229,188))
            image_detail= deb_utility.image_resize(pro_image,(600,600))
            product_image_info = product_image(
                                        product_id=product_id,
                                        product_list=image_list,
                                        product_details=image_detail,
                                        created_date=datetime.now().date(),
                                        )
            product_image_info.save()

    for download_image in download_images:
        down_image= deb_utility.image_resize(download_image,(300,400))
        download_image_info = product_download_image(
                                            product_id=product_id,
                                            download_image=down_image,
                                            created_date=datetime.now().date(),
                                                )
        download_image_info.save() 

    messages.success(request,'Product Inserted Successfully!')
    return redirect(product_list_view)

def product_edit_view(request , product_id):
    product_det=product.objects.filter(id=product_id)
    all_category = category.objects.all().order_by('-id')
    all_brand = brand.objects.all().order_by('-id')

    parent_category_list = category.objects.filter(parent_category = 0)
    sub_category_list = category.objects.filter(~Q(parent_category = 0),Q(sub_category = 0))
    context = {'all_category':all_category, 'parent_category_list': parent_category_list, 'all_brand': all_brand,'product_det':product_det,'sub_category_list':sub_category_list, 'product_active':'active'}
    return render(request, 'product/product_edit_view.html',context)

def product_update(request):
    admin_session_id = request.session['admin_session_id']
    update_product_id = request.POST["update_product_id"]

    category_id = request.POST["category_id"]
    brand_id = request.POST["brand_id"]
    product_name = request.POST["product_name"]
    product_slug = request.POST["product_slug"]
    price_available = request.POST["price_available"]
    gst = request.POST["gst"]
    if gst == '':
        gst = 0.0
    mrp_price = request.POST["mrp_price"]
    sale_price = request.POST["sale_price"]
    discount = request.POST["discount"]
    if price_available == 'no':
        mrp_price = sale_price = discount = 0.0
    qty = request.POST["qty"]
    product_description = request.POST["product_description"]

    product_specification = request.POST["product_specification"]
    product_weight = request.POST["product_weight"]
    product_weight_class = request.POST["product_weight_class"]

    shipping_product_length = request.POST["shipping_product_length"]
    shipping_product_width = request.POST["shipping_product_width"]
    shipping_product_height = request.POST["shipping_product_height"]
    shipping_dimension_class = request.POST["shipping_dimension_class"]
    meta_title = request.POST["meta_title"]
    meta_key = request.POST["meta_key"]
    meta_description = request.POST["meta_description"]

    product_data = product.objects.filter(id=update_product_id)[0]
    product_data.category_id = category_id
    product_data.brand_id = brand_id
    product_data.product_name = product_name
    product_data.product_slug = product_slug
    product_data.product_desc = product_description
    product_data.product_specification = product_specification
    product_data.product_weight = product_weight
    product_data.product_weight_class = product_weight_class
    product_data.available_qty = qty
    product_data.price_available = price_available
    product_data.gst = gst
    product_data.mrp_price = mrp_price
    product_data.discount = discount
    product_data.sell_price = sale_price
    product_data.shipping_dimension_class = shipping_dimension_class
    product_data.shipping_product_height = shipping_product_height
    product_data.shipping_product_length = shipping_product_length
    product_data.shipping_product_width = shipping_product_width
    product_data.meta_title = meta_title
    product_data.meta_keyword = meta_key
    product_data.meta_description = meta_description

    product_data.modified_date = datetime.now().date()
    product_data.modified_by = admin_session_id

    product_data.save(update_fields=[
                                'category_id',
                                'brand_id',
                                'product_name',
                                'product_slug',
                                'product_desc',
                                'product_specification',
                                'product_weight',
                                'product_weight_class',
                                'available_qty',
                                'price_available',
                                'gst',
                                'mrp_price',
                                'discount',
                                'sell_price',
                                'shipping_dimension_class',
                                'shipping_product_height',
                                'shipping_product_length',
                                'shipping_product_width',
                                'meta_title',
                                'meta_keyword',
                                'meta_description',
                                'modified_date',
                                'modified_by']
                                )

    messages.success(request,'Product Updated Successfully!')
    return redirect(product_list_view)

def product_status_change(request):
    status = request.POST['status']
    pro_id = request.POST.getlist('id[]')

    for pro_id in pro_id:
        product_data = product.objects.filter(id=pro_id)[0]
        product_data.product_status = status
        product_data.save(update_fields=['product_status'])

    return JsonResponse({'result': '1'})

def product_delete(request , product_id):
    product_det=product.objects.filter(id=product_id)[0]
    pro_img_det=product_image.objects.filter(product_id=product_id)
    dow_img_det=product_download_image.objects.filter(product_id=product_id)

    for pro_img_det in pro_img_det:
        pro_image_path = pro_img_det.product_list.url
        pro_image_det_path = pro_img_det.product_details.url

        list_image_url = settings.BASE_DIR+pro_image_path
        list_image_url = list_image_url.replace('/','\\')
        os.remove(list_image_url)

        det_image_url = settings.BASE_DIR+pro_image_det_path
        det_image_url = det_image_url.replace('/','\\')
        os.remove(det_image_url)

    for dow_img_det in dow_img_det:
        dow_image_path = dow_img_det.download_image.url

        down_image_url = settings.BASE_DIR+dow_image_path
        down_image_url = down_image_url.replace('/','\\')
        os.remove(down_image_url)

    product_det.delete()
    messages.error(request,'Product Deleted Successfully!')
    return redirect(product_list_view)


# product image functionality
def product_image_list_view(request , product_id):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_pro_img_det=product_image.objects.filter(product_id=product_id)

    context = {'all_pro_img_det': all_pro_img_det,'product_id':product_id,'product_active':'active'}
    return render(request, 'product/product_image_list.html',context)

def product_image_add_view(request , product_id):
    context = {'product_id': product_id,'product_active':'active'}
    return render(request, 'product/product_image_add.html',context)

def product_image_insert(request ):
    product_id = request.POST["product_id"]
    uploaded_image = request.FILES["image"]
    image_list= deb_utility.image_resize(uploaded_image,(229,188))
    image_detail= deb_utility.image_resize(uploaded_image,(600,600))
    product_image_info = product_image(
                                product_id=product_id,
                                product_list=image_list,
                                product_details=image_detail,
                                created_date=datetime.now().date(),
                                )
    product_image_info.save()
    messages.success(request,'Product Image Inserted Successfully!')
    return redirect(product_image_list_view,product_id)

def product_image_delete(request , product_image_id):
	pro_img_det=product_image.objects.filter(id=product_image_id)[0]


	product_id = pro_img_det.product_id
	pro_image_path = pro_img_det.product_list.url
	pro_image_det_path = pro_img_det.product_details.url

	list_image_url = settings.BASE_DIR+pro_image_path
	list_image_url = list_image_url.replace('/','\\')
	os.remove(list_image_url)

	det_image_url = settings.BASE_DIR+pro_image_det_path
	det_image_url = det_image_url.replace('/','\\')
	os.remove(det_image_url)


	pro_img_det.delete()
	messages.error(request,'Product Image Deleted Successfully!')
	return redirect(product_image_list_view,product_id)

def product_image_edit_view(request , product_image_id):
	pro_img_det=product_image.objects.filter(id=product_image_id)
	context = {'pro_img_det': pro_img_det,'product_active':'active'}
	return render(request, 'product/product_image_edit.html',context)

def product_image_update(request):
    pro_image_id = request.POST["pro_image_id"]
    product_id = request.POST["product_id"]

    product_img_data = product_image.objects.filter(id=pro_image_id)[0]
    product_img_data.modified_date = datetime.now().date()

    try:
        if request.FILES["image"]:
            old_image = request.POST["old_image"]
            # print('old_image : ',old_image,settings.BASE_DIR)
            image_url = settings.BASE_DIR+old_image
            image_url = image_url.replace('/','\\')

            os.remove(image_url)
            uploaded_image = request.FILES["image"]
            image_list= deb_utility.image_resize(uploaded_image,(229,188))
            image_detail= deb_utility.image_resize(uploaded_image,(600,600))
            product_img_data.product_list = image_list
            product_img_data.product_details = image_detail

            product_img_data.save(update_fields=['product_list', 'product_details','modified_date'])
        else:
            product_img_data.save(update_fields=['modified_date'])
    except Exception as e:
        product_img_data.save(update_fields=['modified_date'])

    messages.success(request,'Product Image Updated Successfully!')
    return redirect(product_image_list_view,product_id)
###### end of product image##############


# product download image functionality
def product_download_image_list_view(request , product_id):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_pro_download_img_det=product_download_image.objects.filter(product_id=product_id)

    context = {'all_pro_download_img_det': all_pro_download_img_det,'product_id':product_id,'product_active':'active'}
    return render(request, 'product/product_download_image_list.html',context)

def product_download_image_add_view(request , product_id):
    context = {'product_id': product_id,'product_active':'active'}
    return render(request, 'product/product_download_image_add.html',context)

def product_download_image_insert(request ):
    product_id = request.POST["product_id"]
    uploaded_image = request.FILES["image"]
    download_image= deb_utility.image_resize(uploaded_image,(300,400))
    product_download_image_info = product_download_image(
                                product_id=product_id,
                                download_image=download_image,
                                created_date=datetime.now().date(),
                                )
    product_download_image_info.save()
    messages.success(request,'Product Image Inserted Successfully!')
    return redirect(product_download_image_list_view,product_id)

def product_download_image_delete(request , product_download_image_id):
    pro_download_img_det=product_download_image.objects.filter(id=product_download_image_id)[0]


    product_id = pro_download_img_det.product_id
    download_image_path = pro_download_img_det.download_image.url

    list_image_url = settings.BASE_DIR+download_image_path
    list_image_url = list_image_url.replace('/','\\')
    os.remove(list_image_url)
    pro_download_img_det.delete()
    messages.success(request,'Product Image Deleted Successfully!')
    return redirect(product_download_image_list_view,product_id)

def product_download_image_edit_view(request , product_download_image_id):
    pro_download_img_det=product_download_image.objects.filter(id=product_download_image_id)
    context = {'pro_download_img_det': pro_download_img_det,'product_active':'active'}
    return render(request, 'product/product_download_image_edit.html',context)

def product_download_image_update(request):
    pro_download_image_id = request.POST["pro_download_image_id"]
    product_id = request.POST["product_id"]

    product_img_data = product_download_image.objects.filter(id=pro_download_image_id)[0]
    product_img_data.modified_date = datetime.now().date()

    try:
        if request.FILES["image"]:
            old_image = request.POST["old_image"]
            # print('old_image : ',old_image,settings.BASE_DIR)
            image_url = settings.BASE_DIR+old_image
            image_url = image_url.replace('/','\\')

            os.remove(image_url)
            uploaded_image = request.FILES["image"]
            download_image= deb_utility.image_resize(request.FILES["image"],(300,400))
            product_img_data.download_image = download_image

            product_img_data.save(update_fields=['download_image','modified_date'])
        else:
            product_img_data.save(update_fields=['modified_date'])
    except Exception as e:
        product_img_data.save(update_fields=['modified_date'])

    messages.success(request,'Product Download Image Updated Successfully!')
    return redirect(product_download_image_list_view,product_id)

###### end of product download image ###########

# product Addon functionality
def sub_product_list_view(request , product_id):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_sub_products_det=sub_product.objects.filter(product_id=product_id)
    product_name = product.objects.filter(id=product_id)[0].product_name

    context = {'product_name':product_name,'all_sub_products_det': all_sub_products_det,'product_id':product_id,'product_active':'active'}
    return render(request, 'product/sub_product_list.html',context)

def sub_product_add_view(request , product_id):
    product_name = product.objects.filter(id=product_id)[0].product_name
    context = {'product_id': product_id,'product_active':'active', 'product_name':product_name}
    return render(request, 'product/sub_product_add.html',context)

def sub_product_insert(request ):
    admin_session_id = request.session['admin_session_id']
    product_id = request.POST["product_id"]
    sub_product_name = request.POST["sub_product_name"]
    sub_product_price = request.POST["sub_product_price"]
    sub_product_desc = request.POST["sub_product_desc"]
    status = 'active'
    
    sub_product_info = sub_product(
                                product_id=product_id,
                                sub_product_name = sub_product_name,
                                sub_product_price = sub_product_price,
                                sub_product_desc = sub_product_desc,
                                status = status,
                                created_date=datetime.now().date(),
                                created_by = admin_session_id
                                )
    sub_product_info.save()
    messages.success(request,'Sub Product Added Successfully!')
    return redirect(sub_product_list_view,product_id)

def sub_product_delete(request , sub_product_id):
    sub_product_det=sub_product.objects.filter(id=sub_product_id)[0]


    product_id = sub_product_det.product_id
    
    sub_product_det.delete()
    messages.success(request,'Sub Product Deleted Successfully!')
    return redirect(sub_product_list_view,product_id)

def sub_product_edit_view(request , sub_product_id):
    sub_product_det=sub_product.objects.filter(id=sub_product_id)
    if sub_product_det:
        product_name = product.objects.filter(id=sub_product_det[0].product_id)[0].product_name
        context = {'sub_product_det': sub_product_det,'product_active':'active', 'product_name':product_name}
        return render(request, 'product/sub_product_edit.html',context)

def sub_product_update(request):
    admin_session_id = request.session['admin_session_id']
    product_id = request.POST["product_id"]
    sub_product_id = request.POST["sub_product_id"]
    sub_product_name = request.POST["sub_product_name"]
    sub_product_price = request.POST["sub_product_price"]
    sub_product_desc = request.POST["sub_product_desc"]

    sub_product_obj = sub_product.objects.filter(id=sub_product_id)
    if sub_product_obj:
        sub_product_obj[0].sub_product_name= sub_product_name
        sub_product_obj[0].sub_product_price= sub_product_price
        sub_product_obj[0].sub_product_desc= sub_product_desc

        sub_product_obj[0].modified_date = datetime.now().date()
        sub_product_obj[0].modified_by= admin_session_id
        sub_product_obj[0].save(update_fields=['sub_product_name','sub_product_price','sub_product_desc','modified_date','modified_by'])

        messages.success(request,'Sub Product Updated Successfully!')
        return redirect(sub_product_list_view,product_id)
    else:
        messages.success(request,'Sub Product Not Updated Successfully!')
        return redirect(sub_product_list_view,product_id)

def sub_product_status_change(request):
    sub_product_status = request.POST['status']
    sub_product_id_list = request.POST.getlist('id[]')
    
    # print('id list : ', sub_product_id_list)
    for sub_product_id in sub_product_id_list:
        sub_product_data = sub_product.objects.filter(id=sub_product_id)[0]
        sub_product_data.status = sub_product_status
        sub_product_data.save(update_fields=['status'])

    return JsonResponse({'result': '1'})

###### end of sub-product ###########

# Product Review functionality
def product_review_list_view(request, product_id):
    if 'admin_session_id' not in request.session:
        return redirect(accounts.login)

    all_review_objs=review.objects.filter(product_id=product_id)
    product_name = product.objects.filter(id=product_id)[0].product_name

    context = {'product_name':product_name,'all_review_objs': all_review_objs,'product_id':product_id,'product_active':'active'}
    return render(request, 'product/product_review_list_view.html',context)

# check how to delete multiple reviews by seletion
def product_review_delete(request, review_id):
    review_det=review.objects.filter(id=review_id)[0]
    product_id = review_det.product_id
    # print(review_det.message)   
    # review_det.delete()
    messages.success(request,'Product Review Deleted Successfully!')
    return redirect(product_review_list_view,product_id)

