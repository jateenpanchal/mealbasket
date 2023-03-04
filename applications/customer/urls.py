from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name="custhomepage"),
    path('my/<int:id>/', views.my, name="my"),
    path('custreg', views.custreg, name='custreg'),
    path('custlogin', views.custlogin, name='custlogin'),
    path('custlogout', views.custlogout, name='custlogout'),
    path('menu', views.menu, name='menu'),
    path('contact', views.contact, name='contact'),
    path('foodcart', views.foodcart, name='foodcart'),
    path('profilebase', views.profilebase, name='profilebase'),
    path('custprofile', views.custprofile, name='custprofile'),
    path('customerorders', views.customerorders, name='customerorders'),
    path('customerordersdetails', views.customerordersdetails, name='customerordersdetails'),
    path('showuserprofile', views.showuserprofile, name='showuserprofile'),
    path('updateuserprofile/<int:id>/', views.updateuserprofile, name='updateuserprofile'),
    path('catwisefood/<int:id>/', views.catwisefood, name='catwisefood'),
  
    # path("accounts/", include('django.contrib.auth.urls')),


    # cartss

  path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
#     path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]

