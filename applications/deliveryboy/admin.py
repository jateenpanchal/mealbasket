from django.contrib import admin
from .models import *
# Register your models here.


class Deliveryboydataadmin(admin.ModelAdmin):
    list_display= ('id','user')


admin.site.register(Deliveryboydata,Deliveryboydataadmin)