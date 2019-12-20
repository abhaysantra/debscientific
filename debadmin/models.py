from django.db import models
# from tinymce import HTMLField
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField
# from django_mysql.models import EnumField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime

class adminUser(models.Model):
    user_type_id = models.IntegerField()
    full_name = models.CharField(max_length=255)
    login_password = models.CharField(max_length=255)
    login_email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True)
    # admin_status = [
    #     ('active', 'active'),
    #     ('inactive', 'inactive'),
    # ]
    # status = models.CharField(max_length=8, choices=admin_status, default='active')

    gst_no = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)
    pin_code = models.CharField(max_length=255,null=True)
    # country = models.CharField(max_length=255,null=True)
    # state = models.CharField(max_length=255,null=True)
    # city = models.CharField(max_length=255,null=True)
    country = models.IntegerField(null=True)
    state = models.IntegerField(null=True)
    city = models.IntegerField(null=True)

    landmark = models.CharField(max_length=255,null=True)
    profile_image = models.ImageField(upload_to='user_profile' , null=True) #size=[150, 150] ,
    address = models.TextField(null=True)
      
    def __str__(self):
        return self.full_name

class adminEmail(models.Model):
    receive_email = models.CharField(max_length=255)
    from_email = models.CharField(max_length=255)       

    def __str__(self):
        return self.from_email

class slider(models.Model):
    title_1 = models.CharField(max_length=255, null=True)
    title_2 = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='slider', null=True)
    link = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=8, default='active')

    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)


    def __str__(self):
        return self.title_1

class about(models.Model):
    title = models.TextField(null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='about', null=True)
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class gallery(models.Model):
    image = models.ImageField(upload_to='gallery', null=True)
    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.image.url

class contactUs(models.Model):
    address = models.TextField(null=True)
    contact_number = models.CharField(max_length=255, blank=False, null=True)
    land_line_number = models.CharField(max_length=255, blank=False, null=True)
    mail = models.CharField(max_length=255, null=True)
    map_address = models.TextField(null=True)
    footer_content = models.TextField(null=True)
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)

class valuableCustomer(models.Model):
    customer_name = models.CharField(max_length=255, null=True)
    customer_image = models.ImageField(upload_to='valuable_customer', null=True)
    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)

class category(models.Model):
    parent_category = models.IntegerField(null=True)
    sub_category = models.IntegerField(default=0)
    category_name = models.CharField(max_length=255, null=True)
    category_slug = models.CharField(max_length=255, null=True)
    category_image = models.ImageField(upload_to='category', null=True)
    category_status = models.CharField(max_length=8, default='active')
    description = models.TextField(null=True)
    category_commission_fixed = models.CharField(max_length=255, null=True)
    category_commission_percent = models.CharField(max_length=255, null=True)
    category_meta_title = models.CharField(max_length=255, null=True)
    category_meta_description = models.TextField(null=True)
    category_meta_keyword = models.CharField(max_length=255, null=True)
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)


class video(models.Model):
    link = models.CharField(max_length=255, blank=False,null=True)
    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)

class faq(models.Model):
    question = models.TextField(blank=False, null=True)
    answer = models.TextField(blank=False, null=True)

    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)

class brand(models.Model):
    brand_name = models.CharField(max_length=255, null=True)
    brand_image = models.ImageField(upload_to='brand' , null=True)
    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)

class policy(models.Model):
    privacy_policy = models.TextField(blank=False, null=True)
    return_policy = models.TextField(blank=False, null=True)
    terms_of_use = models.TextField(blank=False, null=True)

    status = models.CharField(max_length=8, default='active')
    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)

class banner(models.Model):
    title_1 = models.CharField(max_length=255, null=True)
    title_2 = models.CharField(max_length=255, null=True)
    title_3 = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, null=True)
    banner_image = models.ImageField(upload_to='banner', null=True)
    banner_type = models.CharField(max_length=255, null=True)
    
    created_date = models.DateField(null=True)    
    modified_date = models.DateField(null=True)

    def __str__(self):
        return self.title_1

class product(models.Model):
    category_id = models.IntegerField(null=True)
    brand_id = models.IntegerField(null=True)
    product_name = models.CharField(null=True, max_length=255)
    product_slug = models.CharField(null=True, max_length=255)
    product_desc = models.TextField(null=True)

    available_qty = models.IntegerField(null=True)
    price_available = models.CharField(max_length=8, default='yes')
    mrp_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    gst = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    discount = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    sell_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    product_status = models.CharField(max_length=8, default='active')

    product_specification = models.TextField(null=True)
    product_weight = models.FloatField(null=True)
    product_weight_class = models.CharField(max_length=10, default='kg')

    shipping_product_length = models.FloatField(null=True)
    shipping_product_width = models.FloatField(null=True)
    shipping_product_height = models.FloatField(null=True)
    shipping_dimension_class = models.CharField(null=True, max_length=255)
    meta_title = models.CharField(null=True, max_length=255)
    meta_keyword = models.CharField(null=True, max_length=255)
    meta_description = models.TextField(null=True)
    avg_rating = models.IntegerField(null=True, default=0)
    remaining_rating = models.IntegerField(null=True, default=5)

    created_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    modified_date = models.DateField(null=True)
    modified_by = models.IntegerField(null=True)
    

class product_image(models.Model):
    product_id = models.IntegerField(null=True)
    product_list = models.ImageField(upload_to='product_list' , null=True)
    product_details = models.ImageField(upload_to='product_details', null=True)

    created_date = models.DateField(null=True)
    modified_date = models.DateField(null=True)

class product_download_image(models.Model):
    product_id = models.IntegerField(null=True)
    download_image = models.ImageField(upload_to='product_download_image', null=True)
    
    created_date = models.DateField(null=True)
    modified_date = models.DateField(null=True)

class user_cart_item(models.Model):
    user_id = models.IntegerField(null=True)
    cart_item_id = models.IntegerField(null=True)
    cart_item_qty = models.IntegerField(null=True)
    cart_mrp_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    cart_discount = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    cart_sell_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    addon_id_list = models.TextField(null=True) # JSON-serialized (text) version of your list


class user_wish_list(models.Model):
    user_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)

class billing_address(models.Model):
    user_id = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    gst_no = models.CharField(max_length=256, null=True)
    mobile_number = models.CharField(max_length=255, null=True)
    pincode = models.IntegerField(null=True)
    # country = models.CharField(max_length=255, null=True)
    # state = models.CharField(max_length=255, null=True)
    # city = models.CharField(max_length=255, null=True)
    country = models.IntegerField(null=True)
    state = models.IntegerField(null=True)
    city = models.IntegerField(null=True)
    
    landmark = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
    created_date = models.DateField(null=True)  
    created_by = models.IntegerField(null=True) 

class user_address(models.Model):
    user_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    gst_no = models.CharField(max_length=256, null=True)
    mobile_number = models.CharField(max_length=255, null=True)
    alt_mobile_number = models.CharField(max_length=255, null=True)
    pincode = models.IntegerField(null=True)
    # country = models.CharField(max_length=255, null=True)
    # state = models.CharField(max_length=255, null=True)
    # city = models.CharField(max_length=255, null=True)
    # making them integer field for drop down list purpose
    country = models.IntegerField(null=True)
    state = models.IntegerField(null=True)
    city = models.IntegerField(null=True)


    landmark = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)

    address_type = models.CharField(max_length=8, default='home')

    is_default = models.CharField(max_length=8, default='no')
    post_office = models.CharField(max_length=255,null=True)


    created_date = models.DateField(null=True) 
    created_by = models.IntegerField(null=True) 
    modified_date = models.DateField(null=True) 
    modified_by = models.IntegerField(null=True)   

class order_address(models.Model):
    user_id = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    deli_address_id = models.IntegerField(null=True)
    bill_address_id = models.IntegerField(null=True)

class enquiry(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    created_date = models.DateField(null=True)

class order(models.Model):
    order_unique_id = models.CharField(max_length=256,null=True)
    order_track_id = models.CharField(max_length=256,null=True)
    order_customer_id = models.IntegerField(null=True)
    order_total_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_discount = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_sub_total_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_shipping_charge = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_status = models.CharField(max_length=20, default='Pending')
    payment_method = models.CharField(max_length=8, default='cod')
    payment_status = models.CharField(max_length=8, default='unpaid')
    order_created_date = models.DateField(null=True)

class order_details(models.Model):
    order_id = models.IntegerField(null=True)
    customer_id = models.IntegerField(null=True)
    order_product_id = models.IntegerField(null=True)
    addon_product_id_list = models.TextField(null=True)
    product_seller_id = models.IntegerField(null=True)
    order_product_mrp = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_product_discount = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_product_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    order_product_qty = models.IntegerField(null=True)
    order_product_status = models.CharField(max_length=20, default='Pending')
    return_status = models.CharField(max_length=20, null=True)
    return_reason = models.TextField(null=True)
    cancel_reason = models.TextField(null=True)
    return_date = models.DateField(null=True)
    cancel_date = models.DateField(null=True)
    deliver_date = models.DateField(null=True)

    order_created_date = models.DateField(null=True)

class review(models.Model):
    user_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    remaining_rating = models.IntegerField(null=True)
    message = models.TextField(null=True)
    date = models.DateField(null=True)

class product_enquiry(models.Model):
    product_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    web_address = models.CharField(max_length = 255, null=True)
    message = models.TextField(null=True)

    date = models.DateField(null=True)

class order_invoice(models.Model):
    user_id = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    invoice_number = models.CharField(max_length=255, null=True)
    invoice = models.ImageField(upload_to='generated_invoice', null=True)

    barcode = models.ImageField(upload_to='barcode', null=True)

    created_date = models.DateField(null=True)

class online_payment_details(models.Model):
    user_id = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    payment_id = models.CharField(max_length=255, null=True)
    pay_amount = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    payment_date = models.DateField(null=True)

class pincode_service(models.Model):
    pincode = models.IntegerField(null=True)
    status = models.CharField(max_length=20, default='active')

class sub_product(models.Model):
    product_id = models.IntegerField(null=True)
    sub_product_name = models.CharField(max_length=255, null=True)
    sub_product_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    sub_product_desc = models.TextField(null=True)
    status = models.CharField(max_length=8, default='active')
    
    created_date = models.DateField(null=True) 
    created_by = models.IntegerField(null=True) 
    modified_date = models.DateField(null=True) 
    modified_by = models.IntegerField(null=True)

class user_addon_cart_item(models.Model):
    user_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    cart_id = models.IntegerField(null=True)

    addon_item_id = models.IntegerField(null=True)
    addon_item_sell_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)

class addon_order(models.Model):
    order_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    addon_product_id = models.IntegerField(null=True)
    addon_product_price = models.DecimalField(null=True, decimal_places=2, max_digits=12)

class countries(models.Model):
    country_id = models.IntegerField(null=True)
    sortname = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=250, null=True)
    phonecode = models.IntegerField(null=True)

class states(models.Model):
    state_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    country_id = models.IntegerField(null=True)

class cities(models.Model):
    city_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    state_id = models.IntegerField(null=True)

class otp_service(models.Model):
    phone_number = models.CharField(max_length=255, null=True)
    otp = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
