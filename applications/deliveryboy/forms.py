from django import forms
from.models import Deliveryboydata
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
# from django.forms import ModelForm


class DelRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2','is_deliveryboy')
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Email"})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Password"})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Confirm Password"})
        
    def clean_is_deliveryboy(self):
        is_deliveryboy = self.cleaned_data.get('is_deliveryboy')
        if not is_deliveryboy:
            raise forms.ValidationError("Please indicate whether you are a DeliveryBoy.")
        return is_deliveryboy
        
        
class Deldataform(forms.ModelForm):
    class Meta:
        model = Deliveryboydata
        fields = ['DeliveryBoy_Fullname','DeliveryBoy_PhoneNO','DeliveryBoy_Email','DeliveryBoy_AdharcardNo','DeliveryBoy_DrivingLicenceNo','DeliveryBoy_PanCard']
        # fields = ("__all__")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['DeliveryBoy_Fullname'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your FullName"})
        self.fields['DeliveryBoy_Email'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Email"})
        self.fields['DeliveryBoy_PhoneNO'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your PhoneNumber"})
        self.fields['DeliveryBoy_AdharcardNo'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your AdharCard Number"})
        self.fields['DeliveryBoy_DrivingLicenceNo'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Driving Licence Number"})
        self.fields['DeliveryBoy_PanCard'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Pan Card Number"})
