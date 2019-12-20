from django.urls import path
from debadmin import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_action/', views.login_action, name='login_action'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name='debadmin_index'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('admin_profile_edit/', views.admin_profile_edit, name='admin_profile_edit'),
    path('admin_password_view/', views.admin_password_view, name='admin_password_view'),
    path('admin_password_update/', views.admin_password_update, name='admin_password_update'),
    path('admin_email_view/', views.admin_email_view, name='admin_email_view'),
    path('admin_email_update/', views.admin_email_update, name='admin_email_update'),

    # Manage User List part
    path('user_list_view/', views.user_list_view, name='user_list_view'),
    path('user_delete/<int:user_id>', views.user_delete, name='user_delete'),
    path('user_status_change/', views.user_status_change, name='user_status_change'),

    # Manage Enquiry List part
    path('enquiry_list_view/', views.enquiry_list_view, name='enquiry_list_view'),
    path('enquiry_delete/<int:enquiry_id>', views.enquiry_delete, name='enquiry_delete'),

    # Manage Product Enquiry List
    path('enquiry_product_list_view/', views.enquiry_product_list_view, name='enquiry_product_list_view'),
    path('enquiry_product_delete/<int:enquiry_id>', views.enquiry_product_delete, name='enquiry_product_delete'),

    # Slider part
    path('slider_view/', views.slider_view, name='slider_view'),
    path('slider_add_view/', views.slider_add_view, name='slider_add_view'),
    path('slider_insert/', views.slider_insert, name='slider_insert'),
    path('slider_edit_view/<int:slider_id>', views.slider_edit_view, name='slider_edit_view'),
    path('slider_update/', views.slider_update, name='slider_update'),
    path('slider_status_change/', views.slider_status_change, name='slider_status_change'),

    # Banner part
    path('banner_view/', views.banner_view, name='banner_view'),
    path('banner_add_view/', views.banner_add_view, name='banner_add_view'),
    path('banner_insert/', views.banner_insert, name='banner_insert'),
    path('banner_edit_view/<int:banner_id>', views.banner_edit_view, name='banner_edit_view'),
    path('banner_update/', views.banner_update, name='banner_update'),
    # path('banner_status_change/', views.banner_status_change, name='banner_status_change'),

    # AboutUs part
    path('about_us_add/', views.about_us_add, name='about_us_add'),
    path('about_us_data_insertion/', views.about_us_data_insertion, name='about_us_data_insertion'),

    # Gallery part
    path('gallery_listview/', views.gallery_listview, name='gallery_listview'),
    path('gallery_add_view/', views.gallery_add_view, name='gallery_add_view'),
    path('gallery_insert/', views.gallery_insert, name='gallery_insert'),
    path('gallery_edit_view/<int:gallery_id>', views.gallery_edit_view, name='gallery_edit_view'),
    path('gallery_update/', views.gallery_update, name='gallery_update'),
    path('gallery_status_change/', views.gallery_status_change, name='gallery_status_change'),
    path('gallery_delete/<int:gallery_id>', views.gallery_delete, name='gallery_delete'),

    # Manage Pincode part
    path('pincode_service_listview/', views.pincode_service_listview, name='pincode_service_listview'),
    path('pincode_service_add_view/', views.pincode_service_add_view, name='pincode_service_add_view'),
    path('pincode_service_insert/', views.pincode_service_insert, name='pincode_service_insert'),
    path('pincode_service_edit_view/<int:pincode_service_id>', views.pincode_service_edit_view, name='pincode_service_edit_view'),
    path('pincode_availability_check/', views.pincode_availability_check, name='pincode_availability_check'),
    path('pincode_service_status_change/', views.pincode_service_status_change, name='pincode_service_status_change'),
    path('pincode_service_delete/<int:pincode_service_id>', views.pincode_service_delete, name='pincode_service_delete'),
    path('pincode_service_add_bulk_pincode_view/', views.pincode_service_add_bulk_pincode_view, name='pincode_service_add_bulk_pincode_view'),
    path('pincode_service_add_bulk_pincode/', views.pincode_service_add_bulk_pincode, name='pincode_service_add_bulk_pincode'),

    # contactUs part
    path('contact_us_add/', views.contact_us_add, name='contact_us_add'),
    path('contact_us_data_insertion/', views.contact_us_data_insertion, name='contact_us_data_insertion'),

    # valuable customer part
    path('valuable_customer_view/', views.valuable_customer_view, name='valuable_customer_view'),
    path('valuable_customer_add_view/', views.valuable_customer_add_view, name='valuable_customer_add_view'),
    path('valuable_customer_insert/', views.valuable_customer_insert, name='valuable_customer_insert'),
    path('valuable_customer_edit_view/<int:valuable_customer_id>', views.valuable_customer_edit_view, name='valuable_customer_edit_view'),
    path('valuable_customer_update/', views.valuable_customer_update, name='valuable_customer_update'),
    path('valuable_customer_status_change/', views.valuable_customer_status_change, name='valuable_customer_status_change'),
    path('valuable_customer_delete/<int:valuable_customer_id>', views.valuable_customer_delete, name='valuable_customer_delete'),
    
    #category part
    path('category_listview/', views.category_listview, name='category_listview'),
    path('category_add_view/', views.category_add_view, name='category_add_view'),
    path('category_insert/', views.category_insert, name='category_insert'),
    path('category_edit_view/<int:category_id>', views.category_edit_view, name='category_edit_view'),
    path('category_delete/<int:category_id>', views.category_delete, name='category_delete'),
    path('category_update/', views.category_update, name='category_update'),
    path('category_status_change/', views.category_status_change, name='category_status_change'),
    path('get_subcategory/', views.get_subcategory, name='get_subcategory'),

    #brand part
    path('brand_list_view/', views.brand_list_view, name='brand_list_view'),
    path('brand_add_view/', views.brand_add_view, name='brand_add_view'),
    path('brand_insert/', views.brand_insert, name='brand_insert'),
    path('brand_edit_view/<int:brand_id>', views.brand_edit_view, name='brand_edit_view'),
    path('brand_delete/<int:brand_id>', views.brand_delete, name='brand_delete'),
    path('brand_update/', views.brand_update, name='brand_update'),
    path('brand_status_change/', views.brand_status_change, name='brand_status_change'),

    # video part
    path('video_view/', views.video_view, name='video_view'),
    path('video_add_view/', views.video_add_view, name='video_add_view'),
    path('video_insert/', views.video_insert, name='video_insert'),
    path('video_edit_view/<int:video_id>', views.video_edit_view, name='video_edit_view'),
    path('video_update/', views.video_update, name='video_update'),
    path('video_status_change/', views.video_status_change, name='video_status_change'),
    path('video_delete/<int:video_id>', views.video_delete, name='video_delete'),

    # faq part
    path('faq_list_view/', views.faq_list_view, name='faq_list_view'),
    path('faq_add_view/', views.faq_add_view, name='faq_add_view'),
    path('faq_insert/', views.faq_insert, name='faq_insert'),
    path('faq_edit_view/<int:faq_id>', views.faq_edit_view, name='faq_edit_view'),
    path('faq_update/', views.faq_update, name='faq_update'),
    path('faq_status_change/', views.faq_status_change, name='faq_status_change'),
    path('faq_delete/<int:faq_id>', views.faq_delete, name='faq_delete'),

    # Policy part
    path('policy_add/', views.policy_add, name='policy_add'),
    path('policy_data_insertion/', views.policy_data_insertion, name='policy_data_insertion'),

    #product part
    path('product_list_view/', views.product_list_view, name='product_list_view'),
    path('product_add_view/', views.product_add_view, name='product_add_view'),
    path('product_insert/', views.product_insert, name='product_insert'),
    path('product_edit_view/<int:product_id>', views.product_edit_view, name='product_edit_view'),
    path('product_delete/<int:product_id>', views.product_delete, name='product_delete'),
    path('product_update/', views.product_update, name='product_update'),
    path('product_status_change/', views.product_status_change, name='product_status_change'), 
    # for product image part   
    path('product_image_list_view/<int:product_id>', views.product_image_list_view, name='product_image_list_view'),
    path('product_image_add_view/<int:product_id>', views.product_image_add_view, name='product_image_add_view'),
    path('product_image_insert/', views.product_image_insert, name='product_image_insert'),
    path('product_image_delete/<int:product_image_id>', views.product_image_delete, name='product_image_delete'),
    path('product_image_edit_view/<int:product_image_id>', views.product_image_edit_view, name='product_image_edit_view'),
    path('product_image_update/', views.product_image_update, name='product_image_update'),

    # for product download image part   
    path('product_download_image_list_view/<int:product_id>', views.product_download_image_list_view, name='product_download_image_list_view'),
    path('product_download_image_add_view/<int:product_id>', views.product_download_image_add_view, name='product_download_image_add_view'),
    path('product_download_image_insert/', views.product_download_image_insert, name='product_download_image_insert'),
    path('product_download_image_delete/<int:product_download_image_id>', views.product_download_image_delete, name='product_download_image_delete'),
    path('product_download_image_edit_view/<int:product_download_image_id>', views.product_download_image_edit_view, name='product_download_image_edit_view'),
    path('product_download_image_update/', views.product_download_image_update, name='product_download_image_update'),

    # for product Addon part   
    path('sub_product_list_view/<int:product_id>', views.sub_product_list_view, name='sub_product_list_view'),
    path('sub_product_add_view/<int:product_id>', views.sub_product_add_view, name='sub_product_add_view'),
    path('sub_product_insert/', views.sub_product_insert, name='sub_product_insert'),
    path('sub_product_delete/<int:sub_product_id>', views.sub_product_delete, name='sub_product_delete'),
    path('sub_product_edit_view/<int:sub_product_id>', views.sub_product_edit_view, name='sub_product_edit_view'),
    path('sub_product_update/', views.sub_product_update, name='sub_product_update'),
    path('sub_product_status_change/', views.sub_product_status_change, name='sub_product_status_change'),

    # for product Review part   
    path('product_review_list_view/<int:product_id>', views.product_review_list_view, name='product_review_list_view'),
    path('product_review_delete/<int:review_id>', views.product_review_delete, name='product_review_delete'),
    # path('product_review_delete_multiple/', views.product_review_delete, name='product_review_delete'),
    
    # Manage Order List part
    path('order_list_view/', views.order_list_view, name='order_list_view'),
    path('change_order_status/', views.change_order_status, name='change_order_status'),
    path('change_return_status/', views.change_return_status, name='change_return_status'),
    path('change_order_details_status/', views.change_order_details_status, name='change_order_details_status'),
    path('order_details_view/<int:order_id>', views.order_details_view, name='order_details_view'),
    path('generate_pdf_from_html/<int:order_id>', views.generate_pdf_from_html, name='generate_pdf_from_html'),
    path('low_stock_list_view/', views.low_stock_list_view, name='low_stock_list_view'),
        
]