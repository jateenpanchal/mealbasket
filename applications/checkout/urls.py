from django.urls import path
from .import views
urlpatterns = [
    path("",views.CheckOut,name='CheckOut'),
    path("handlerequest",views.handlerequest,name='handlerequest'),
]