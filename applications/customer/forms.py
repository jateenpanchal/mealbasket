# from django.contrib.auth.models import User
from django import forms
from.models import Profile
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

# customer data (customer profile form)
class custdataform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Customer_Fullname','Customer_Email','Customer_Phoneno','Customer_Address']
        # fields = ("__all__")
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['Customer_Fullname'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your FullName"})
        self.fields['Customer_Email'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Email"})
        self.fields['Customer_Phoneno'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your PhoneNumber"})
        self.fields['Customer_Address'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Address"})
        
 
 
#  customer registration form
class CustRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2','is_customer')
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Email"})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Password"})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Confirm Password"})
        
    def clean_is_customer(self):
        is_customer = self.cleaned_data.get('is_customer')
        if not is_customer:
            raise forms.ValidationError("Please indicate whether you are a customer.")
        return is_customer
        
        
# from django.contrib.auth.forms import PasswordResetForm
# class UserPasswordResetForm(PasswordResetForm):
#     def __init__(self, *args, **kwargs):
#         super(UserPasswordResetForm, self).__init__(*args, **kwargs)

#     email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'email',
#         'type': 'email',
#         'name': 'email'
#         }))