from django.contrib import admin
from.models import Profile

class Profileadmin(admin.ModelAdmin):
    list_display= ('id','user', 'Customer_Fullname', 'Customer_Email', 'Customer_Phoneno','Customer_Address')


admin.site.register(Profile,Profileadmin)