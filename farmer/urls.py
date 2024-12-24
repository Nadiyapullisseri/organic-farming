from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
 
urlpatterns=[
    path('',views.index),
    path('register/',views.reg,name='registers'),
    path('register/login/',views.login_view,name='logins'),
    path('dashboard',views.dashboard_view,name='dashboard'),
    path('farmer-register/',views.farmer_register,name='farmer-registers'),
    path('farmer-register/login/',views.farmer_login_view,name='farmer-logins'),
    path('farmer-dashboard',views.farmer_dashboard_view,name='farmer-dashboard'),
    path('admin-login',views.admin_login_view,name='admin-logins'),
    path('admin-dashboard',views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-users',views.admin_users_view,name='admin-users'),
    path('admin-farmers',views.admin_farmers_view,name='admin-farmers'),
    path('admin-feedback',views.admin_feedback_view,name='admin-feedback'),
    path('update-admin-users/<int:pk>',views.update_admin_users_view,name='update-admin-users'),
    path('delete-admin-user/<int:pk>',views.delete_admin_users_view,name='delete-admin-users'),
    path('update-admin-farmers/<int:pk>',views.update_admin_farmers_view,name='update-admin-farmers'),
    path('delete-admin-farmers/<int:pk>',views.delete_admin_farmers_view,name='delete-admin-farmers'),
    path('farmer-product',views.farmer_product_view,name='farmer-product'),
    path('farmer-add-product',views.farmer_add_product_view,name='farmer-add-product'),
    path('edit-farmer-product/<int:pk>',views.edit_farmer_product_view,name='edit-farmer-product'),
    path('delete-farmer-product/<int:pk>',views.delete_farmer_product_view,name='delete-farmer-product'),
    path('customer-product',views.customer_product_view,name='customer-product'),
    path('customer-feedback',views.customer_feedback_view,name='customer-feedback'),
    path('farmer-query',views.farmer_query_view,name='farmer-query'),
    path('error-page',views.error_page_view,name='error-page'),
    path('question-view',views.question_view,name='question-view'),
    path('admin-query',views.admin_query_view,name='admin-query'),
    path('update-admin-query/<int:pk>',views.update_admin_query_view,name='update-admin-query'),
    path('admin-notice',views.admin_notices_view,name='admin-notice'),
    path('farmer-notice-view',views.farmer_notice_view,name='farmer-notice-view'),
    path('admin-notice-view',views.admin_notice_view,name='admin-notice-view'),
    path('cart-page',views.cart_page_view,name='cart-page'),
    path('add-to-cart/<int:pk>',views.add_to_cart_view,name='add-to-cart'),
    path('remove-from-cart/<int:pk>',views.remove_from_cart_view,name='remove-from-cart'),
    path('cart-pay',views.cart_pay_view,name='cart-pay'),
    path('payment-page',views.payment_page_view,name='payment-page'),
    path('admin-payment-view',views.admin_payment_view,name='admin-payment-view'),
    path('cart-search',views.cart_search_view,name='cart-search'),
    path('contact-us',views.contact_us_view,name='contact-us'),
    path('customer-logout',views.customer_logout_view,name='customer-logout'),
    path('farmer-logout',views.farmer_logout_view,name='farmer-logout'),
    path('admin-logout',views.farmer_logout_view,name='admin-logout'),
    path('farmer-profile/<int:id>',views.farmer_profile_view,name='farmer-profile'),









    

















]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
