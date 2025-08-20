from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from Services.models import Services
from .models import Otp

class Verfiy(forms.ModelForm):
    
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
    
    
   
        