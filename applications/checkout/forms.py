from .models import Order
from django import forms

class orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields ='__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control ','placeholder':"Enter Your First Name"})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Last Name"})
        self.fields['order_status'].widget.attrs.update({'class':'form-select'})
        self.fields['order_total'].widget.attrs.update({'type':'hidden','class':'form-select'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Contact Number"})
        self.fields['address'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Address"})
        self.fields['state'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your State"})
        self.fields['city'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your City"})
        self.fields['area'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Area"})
        self.fields['pin_code'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Confirm Pin-Code"})

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status']
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['order_status'].widget.attrs.update({'class':'form-select'})

class DeliveryStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_status']
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['delivery_status'].widget.attrs.update({'class':'form-select'})

class DelOrderChoice(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_order_choice']
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['delivery_order_choice'].widget.attrs.update({'class':'form-select'})
        