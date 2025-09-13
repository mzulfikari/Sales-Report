from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from Services.models import Services


class Plaque(forms.MultiWidget):
    """     
    To implement the appearance of the license plate number form in the template
    """
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(
                attrs={'maxlength': '2', 
                       'class': 'form-control plaque-input text-center fw-bold border rounded shadow-sm',
                       'style': 'width: 60px; letter-spacing: 2px;',
                       }),
             forms.TextInput(
                attrs={'maxlength': '1',
                       'class': 'form-control plaque-input text-center fw-bold border rounded shadow-sm',
                       'style': 'width: 50px; letter-spacing: 2px;',
                       'placeholder': 'الف'}),
           
            forms.TextInput(
                attrs={'maxlength': '3',
                       'class': 'form-control plaque-input text-center fw-bold border rounded shadow-sm', 
                       'style': 'width: 80px; letter-spacing: 2px;',
                       }),
            
            forms.TextInput(
                attrs={'maxlength': '2',
                       'class': 'form-control plaque-input text-center fw-bold border rounded shadow-sm',
                       'style': 'width: 60px; letter-spacing: 2px;',
                       }),
        ]
        super().__init__(widgets, attrs)
        
    def decompress(self, value):
     if value:
        return value.split("-")
     return ["", "", "", ""]
    
    
class PlateField(forms.MultiValueField):
    """
    Unifying the license plate number inputs and then saving in the field related to the license plate 
    """
    def __init__(self, *args, **kwargs):
        fields = [
            forms.CharField(max_length=2),
            forms.CharField(max_length=1),
            forms.CharField(max_length=3),
            forms.CharField(max_length=2),
        ]
        super().__init__(fields, widget=Plaque(), *args, **kwargs)

    def compress(self, data_list):
     if data_list:
        return "-".join(data_list)


class InformationCar(forms.ModelForm):
    """Vehicle registration form"""
    sold_by = forms.IntegerField(required=False)
    plaque = PlateField(label=' شماره پلاک :')
    
    class Meta:
        model = Services   
        fields  = ('customer_phone','car','car_model','color','current_km',)
        labels = {
            'customer_phone': 'شماره تلفن :',
            'car': 'نام خودرو :',
            'car_model': ' مدل خودرو :',
            'color': 'رنگ',
            'current_km': ' کیلومترفعلی :',
        }
        
        widgets = {
            'customer_phone': forms.TextInput(
            attrs={
            'class': "form-control text-right ltr numeric",
            'inputmode': 'numeric',
            'pattern': '[0-9]*',
            }),
            'car': forms.TextInput(
            attrs={'class':
            "form-control",
            }),
            'car_model': forms.NumberInput(
            attrs={'class':
            "form-control",
            }),
            'current_km': forms.TextInput(
            attrs={'class':
            "form-control text-right ltr numeric",
            }),
        }
        
        
    def clean_customer_phone(self):
        """ Verification of telephone number entry in Iran """
        customer_phone = self.cleaned_data.get('customer_phone')
        if not customer_phone:
            raise ValidationError("شماره تلفن الزامی است.")
        if customer_phone:
            if not customer_phone.startswith('09'):
                raise ValidationError("شماره تلفن باید با 09 شروع شود.")
            if len(customer_phone) != 11:
                raise ValidationError("شماره تلفن باید 11 رقم باشد.")
        return customer_phone
    
    
    def clean_car(self):
        """ Error handling for vehicle names """
        car = self.cleaned_data.get('car')
        if len(car) < 3:
            raise ValidationError("نام خودرو حدداقل باید سه حرف باشد.")
        if len(car) > 30:
            raise ValidationError("نام خودرو حداکثر باید سی حرف باشد..")
        return car
    
    
    def clean_car_model(self):
        """ Error handling for vehicle models"""
        car_model = self.cleaned_data.get('car_model')
        if not car_model:
         return None
        if not str(car_model).isdigit():
             raise forms.ValidationError('مدل خودرو باید فقط شامل عدد باشد.')
        if len(car_model) < 2 or len(car_model) > 4:
            raise forms.ValidationError('مدل خودرو باید بین 2 تا 4 رقم باشد.')
        return car_model
    
    
    def clean_current_km(self):
     current_km = self.cleaned_data.get('current_km')
     if not current_km:
        return None
     try:
         current_km = float(current_km)
     except (ValueError, TypeError):
        raise ValidationError("کیلومتر باید یک عدد معتبر باشد.")
     if current_km < 0:
        raise ValidationError("کیلومتر نمی‌تواند منفی باشد.")
     return current_km
 