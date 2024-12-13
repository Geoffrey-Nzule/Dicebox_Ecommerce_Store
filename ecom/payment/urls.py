from django.urls import path, include
from django.contrib import admin
from . import views 

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
  
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name='billing_info'),
    path('process_order', views.process_order, name='process_order'),
    path('shipped_dash', views.shipped_dash, name="shipped_dash"),
    path('not_shipped_dash', views.not_shipped_dash, name="not_shipped_dash"),
    path('orders/<int:pk>', views.orders, name='orders'),
    path('', views.payment_view, name='payment'),
    path('callback/', views.payment_callback, name='payment_callback'),
    path('stk-status/', views.stk_status_view, name='stk_status'),
    path('process-mpesa-payment/', views.process_mpesa_payment, name='process_mpesa_payment'),
    
 

   
]