from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name="custhomepage"),
    path('my/<int:id>/', views.my, name="my"),
    path('custreg', views.custreg, name='custreg'),
    path('search_results', views.search_results, name='search_results'),
    path('custlogin', views.custlogin, name='custlogin'),
    path('custlogout', views.custlogout, name='custlogout'),
    path('menu', views.menu, name='menu'),
    path('contact', views.contact, name='contact'),
    path('foodcart', views.foodcart, name='foodcart'),
    path('payment', views.payment, name='payment'),
    path('profilebase', views.profilebase, name='profilebase'),
    path('custprofile', views.custprofile, name='custprofile'),
    path('customerorders', views.customerorders, name='customerorders'),
    path('customerordersdetails', views.customerordersdetails,
         name='customerordersdetails'),
    path('showuserprofile', views.showuserprofile, name='showuserprofile'),
    path('updateuserprofile/<int:id>/',views.updateuserprofile, name='updateuserprofile'),
#     path('deletprofile/<int:id>/',views.deletprofile, name='deletprofile'),
    path('catwisefood/<int:id>/', views.catwisefood, name='catwisefood'),


    # cartss
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('buy_now/<int:id>/', views.buy_now, name='buy_now'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
