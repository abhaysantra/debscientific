from django.urls import path
from debfrontend import views

urlpatterns = [
    path('', views.index, name='index'),

    #login & registration part
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register_submit/', views.register_submit, name='register_submit'),
    path('user_login_action/', views.user_login_action, name='user_login_action'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('validate_email_id/', views.validate_email_id, name='validate_email_id'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('fetch_password_n_send/', views.fetch_password_n_send, name='fetch_password_n_send'),
    

    #dashboard
    path('user-dashboard/', views.dashboard, name='dashboard'),

    #password-change
    path('change-password/', views.change_password, name='change_password'),
    path('change_password_submit/', views.change_password_submit, name='change_password_submit'),

    #profile
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user_profile_update/', views.user_profile_update, name='user_profile_update'),

    #footer pages
    path('about-us/', views.about_us, name='about_us'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('faq/', views.faq_view, name='faq_view'),
    path('return-policy/', views.return_policy_view, name='return_policy_view'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy_view'),
    path('terms-of-use/', views.terms_of_use_view, name='terms_of_use_view'),
    path('contact-us/', views.contact_us_view, name='contact_us_view'),
    path('our-valuable-customer/', views.our_valuable_customer, name='our_valuable_customer'),
    path('video/', views.video_list, name='video_list'),

    #add to cart
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    # special case for direct_buy_now button when addon product must before buying
    path('direct_buy_now/', views.direct_buy_now, name='direct_buy_now'),
    
    path('add_single_to_cart/', views.add_single_to_cart, name='add_single_to_cart'),
    path('update_cart_item_qty/', views.update_cart_item_qty, name='update_cart_item_qty'),
    path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('view-cart/', views.view_cart, name='view_cart'),
    #without login cart data delete
    path('session_cart_item_delete/', views.session_cart_item_delete, name='session_cart_item_delete'),
    path('update_sess_cart_item_qty/', views.update_sess_cart_item_qty, name='update_sess_cart_item_qty'),

    #checkout
    path('order-summary/', views.order_summary, name='order_summary'),
    path('check_pincode_service/', views.check_pincode_service, name='check_pincode_service'),
    path('delivery-address/', views.delivery_address, name='delivery_address'),
    path('get_default_delivery_add/', views.get_default_delivery_add, name='get_default_delivery_add'),
    path('submit_billing_address/', views.submit_billing_address, name='submit_billing_address'),
    path('place-order/', views.place_order, name='place_order'),
    path('payment/', views.payment, name='payment'),
    path('order_submit_action/', views.order_submit_action, name='order_submit_action'),
    path('completation/', views.completation, name='completation'),

    #add to wishlist
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('remove_wishlist_after_cart/', views.remove_wishlist_after_cart, name='remove_wishlist_after_cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist-dashboard/', views.my_wishlist, name='my_wishlist'),

    #enquiry
    path('enquery_form_submit/', views.enquery_form_submit, name='enquery_form_submit'),

    #my order
    path('my-order/', views.my_order, name='my_order'),
    path('order-details/<int:order_id>/<str:uniqu_id>/', views.order_details_view, name='order_details_view'),
    path('cancel_single_order/', views.cancel_single_order, name='cancel_single_order'),
    path('cancel_reason_submit/', views.cancel_reason_submit, name='cancel_reason_submit'),
    path('return_reason_submit/', views.return_reason_submit, name='return_reason_submit'),

    #notification
    path('my-notification/', views.my_notification, name='my_notification'),

    #wallet
    path('my-wallet/', views.my_wallet, name='my_wallet'),
    
    #manage address : User Address user_address_delete
    path('manage-address/', views.my_address_list, name='my_address_list'),
    path('add-new-address/', views.add_new_address, name='add_new_address'),
    path('insert_new_address/', views.insert_new_address, name='insert_new_address'),
    path('change-address-status/', views.change_address_status, name='change_address_status'),
    path('user_address_delete/', views.user_address_delete, name='user_address_delete'),
    path('user-address-edit-view/<int:user_address_id>', views.user_address_edit_view, name='user_address_edit_view'),
    path('user-address-update/<int:user_address_id>', views.user_address_update, name='user_address_update'),


    #product list & details
    path('product-list/<int:cat_id>/<str:cat_slug>', views.product_list, name='product_list'),
    path('product-details/<int:product_id>/<str:product_slug>', views.product_details, name='product_details'),
    path('review_submit/', views.review_submit, name='review_submit'),
    path('product-enquiry-view/<int:enquiry_product_id>', views.product_enquiry_view, name='product_enquiry_view'),
    path('product-enquiry-submission/', views.product_enquiry_submission, name='product_enquiry_submission'),
    path('product-search/', views.product_search, name='product_search'),
    path('autocomplete_product_name/', views.autocomplete_product_name, name='autocomplete_product_name'),
    path('get_filter_product_list/', views.get_filter_product_list, name='get_filter_product_list'),
    # to get list of addon products for any particular product
    path('get_addon_total_price/', views.get_addon_total_price, name='get_addon_total_price'),
    path('get_addon_product_list/', views.get_addon_product_list, name='get_addon_product_list'),
    # to get filtered product list based on min-max price
    # path('filtered_product_list/', views.filtered_product_list, name='filtered_product_list'),

    # get state list based on selected country id
    path('get_state_list/', views.get_state_list, name='get_state_list'),
    path('get_city_list/', views.get_city_list, name='get_city_list'),
    path('get_country_state_city_name/', views.get_country_state_city_name, name='get_country_state_city_name'),
    
    #otp check
    path('check_otp_service/', views.check_otp_service, name='check_otp_service'),
    path('resend_otp/', views.resend_otp, name='resend_otp'),


]