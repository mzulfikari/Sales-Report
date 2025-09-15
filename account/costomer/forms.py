from django import forms
from django.core.exceptions import ValidationError


class CustomerVerfiy(forms.Form):
    
    phone_customer = forms.CharField(
        label="شماره موبایل",
        widget=forms.TextInput(attrs={
            'class': 'form-control ltr text-left',
            'style': 'width:350px; height:30px;',
        })
    )
   
    def clean_phone(self):
         customer_phone= self.cleaned_data.get('customer_phone')
         if not customer_phone.startswith('09'):
            raise ValidationError("شماره تلفن باید با 09 شروع شود.")
         if len(customer_phone) != 11:
            raise ValidationError("شماره تلفن باید 11 رقم باشد.")
         return customer_phone

        