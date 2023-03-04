from django.urls import path,include
from .import views
urlpatterns = [
    path("deldataform",views.Deliveryboydata,name='deldataform'),
    path("delsidebar",views.delsidebar,name='delsidebar'),
    path("",views.delhomepage,name='delhomepage'),
    path("delreg",views.delreg,name='delreg'),
    path("dellogin",views.dellogin,name='dellogin'),
    path("dellogout",views.dellogout,name='dellogout'),
    path("delorders",views.delorders,name='delorders'),
    path("acceptedorder",views.acceptedorder,name='acceptedorder'),
    path("rejectedorder",views.rejectedorder,name='rejectedorder'),
    path("moreorderdetail/<int:id>/",views.moreorderdetail,name='moreorderdetail'),
    path("updateorders/<int:id>/",views.updateorders,name='updateorders'),
    path("updatedelstatus/<int:id>/",views.updatedelstatus,name='updatedelstatus'),
    path("updatedelprofile/<int:id>/",views.updatedelprofile,name='updatedelprofile'),
    # path("updateorders",views.updateorders,name='updateorders'),
    path("showdelprofile",views.showdelprofile,name='showdelprofile'),
    path("deldashboard",views.deldashboard,name='deldashboard'),
]