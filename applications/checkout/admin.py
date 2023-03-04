from django.contrib import admin
from .models import Order

# Register your models here.
# Register your models here.

class Orderadmin(admin.ModelAdmin):
    list_display= ('user', "f_name",'first_name', 'last_name', 'phone_number','total','quantity',)

admin.site.register(Order,Orderadmin)