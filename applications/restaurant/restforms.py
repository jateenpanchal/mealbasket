from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class restregform(UserCreationForm):
    r_name = forms.CharField()
    r_address = forms.CharField()
    r_type = forms.ChoiceField(widget = forms.Select(), 
                 choices = ([('V','Veg'), ('N','Non-Veg'),('B','Veg & Non-Veg'), ]), initial='3', required = True,)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','r_name','r_address','r_type']    