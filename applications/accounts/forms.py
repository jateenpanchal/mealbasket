from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2')
        