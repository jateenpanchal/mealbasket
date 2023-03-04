from django.contrib import admin
from .models import *
# from .models import restdata
# Register your models here.


class useradminview(admin.ModelAdmin):
    list_display = ['category_name','food_name','food_price','food_photo']
admin.site.register(fooditemdata,useradminview)

class useradminview(admin.ModelAdmin):
    list_display = ['user','Restaurant_Name','Restaurant_Email','Restaurant_Type','Restaurant_GSTno']
admin.site.register(Restaurant_data,useradminview)

# admin.site.register(restdata)