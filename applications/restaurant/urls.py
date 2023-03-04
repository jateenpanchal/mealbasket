from django.urls import path,include
from .import views
urlpatterns = [
    # path("rest",views.index,name='restreg'),
    # path("restlogin",views.restdatalogin,name='restlogin'),
    path("",views.resthomepage,name='resthomepage'),
    path("restreg",views.restreg,name='restreg'),
    path("restlogin",views.restlogin,name='restlogin'),
    path("restlogout",views.restlogout,name='restlogout'),
    path("addfooditem",views.addfooditem,name='addfooditem'),
    path("restfoodmenu/",views.restfoodmenu,name='restfoodmenu'),
    path("restdata",views.Restaurantdata,name='restdata'),
    path("restdashbord",views.restdashbord,name='restdashbord'),
    path("custorders",views.custorders,name='custorders'),
    path("showrestprofile",views.showrestprofile,name='showrestprofile'),
    path("updaterestprofile/<int:id>/",views.updaterestprofile,name='updaterestprofile'),
    path("restupdateorders/<int:id>/",views.restupdateorders,name='restupdateorders'),
    path("deletfooditem/<int:id>/",views.deletfooditem,name='deletfooditem'),
    path("updatefooditem/<int:id>/",views.updatefooditem,name='updatefooditem'),
]