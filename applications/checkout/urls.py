from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.CheckOut,name='CheckOut'),
    path("handlerequest",views.handlerequest,name='handlerequest'),
    
    path('complete/', views.paymentComplete, name="complete"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]