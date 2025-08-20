from django import forms
from django.core.exceptions import ValidationError
from Services.models import Services

class CustomerVerfiy(forms.ModelForm):
    
    class Meta:
        model = Services        
        fields = ('customer_phone',)
        labels = {'customer_phone': 'شماره موبایل',}
        
        widgets = {
        'customer_phone': forms.TextInput(
        attrs={'class':
        "input-group",
        'type':'tel',
        'id': 'mobile',
        })}
        
    def clean_phone(self):
         customer_phone= self.cleaned_data.get('customer_phone')
         if not customer_phone.startswith('09'):
            raise ValidationError("شماره تلفن باید با 09 شروع شود.")
         if len(customer_phone) != 11:
            raise ValidationError("شماره تلفن باید 11 رقم باشد.")
         return customer_phone

        