from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from Services.models import Services
from ..models import Otp

class CustomerVerfiy(forms.ModelForm):
    
    class Meta:
        model = Services
        
        fields = ('phone',)
        labels = {'phone': 'شماره موبایل',}
        
        widgets = {
        'phone': forms.TextInput(
        attrs={'class':
        "input-group",
        'type':'tel',
        
        })}
        
    def clean_phone(self):
         phone = self.cleaned_data.get('phone')
         if not phone.startswith('09'):
            raise ValidationError("شماره تلفن باید با 09 شروع شود.")
         if len(phone) != 11:
            raise ValidationError("شماره تلفن باید 11 رقم باشد.")
         return phone


class VerfiyCustomer(forms.ModelForm):
    
    class Meta:
        model = Otp
        fields = ['code']
    
    code = forms.ChoiceField(
       widget=forms.HiddenInput()
    )
    
    def clean_code(self):
        code = self.cleaned_data.get('code')

        if not code:
            raise ValidationError("لطفاً کد تأیید را وارد کنید.")

        if len(code) != 4:
            raise ValidationError("کد باید دقیقاً ۴ رقم باشد.")

        return code
    
    
   
        