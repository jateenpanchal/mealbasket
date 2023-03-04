from django import forms
from .models import *
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class fooditemdataform(forms.ModelForm):
    class Meta:
        model = fooditemdata
        fields = ['category_name','food_name','food_price','food_photo',"availability"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({  
        'class': 'form-select',
        'aria-label': 'Default select example'})
        self.fields['food_name'].widget.attrs.update({'class':' form-control'})
        self.fields['food_price'].widget.attrs.update({'class':"form-control"})
        self.fields['food_photo'].widget.attrs.update({'class':"form-control"})

        
class restdataform(forms.ModelForm):
    class Meta:
        model = Restaurant_data
        # fields = ("__all__")
        fields = ['Restaurant_Name','Restaurant_Phoneno','Restaurant_Email','Restaurant_Type','Restaurant_Address','Restaurant_GSTno']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Restaurant_Name'].widget.attrs.update({'class':'form-control'})
        self.fields['Restaurant_Email'].widget.attrs.update({'class':'form-control'})
        self.fields['Restaurant_Phoneno'].widget.attrs.update({'class':'form-control'})
        self.fields['Restaurant_Type'].widget.attrs.update({'class':'form-select'})
        self.fields['Restaurant_Address'].widget.attrs.update({'class':'form-control'})
        self.fields['Restaurant_GSTno'].widget.attrs.update({'class':'form-control'})
        
        

class RestRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2','is_restaurantowner')
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Email"})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Password"})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Confirm Password"})
    
    def clean_is_restaurant(self):
        is_restaurantowner = self.cleaned_data.get('is_restaurantowner')
        if not is_restaurantowner:
            raise forms.ValidationError("Please indicate whether you are a Restaurant Owner.")
        return is_restaurantowner
    
        
        
    