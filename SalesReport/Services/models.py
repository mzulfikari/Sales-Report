from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext as _
from Store.models import Store,Product
from account.models import Costumer
from account.models import User


class Services(models.Model):
    """
    Implementation of services with the ability to register a store with limited access to the admin
    Connecting to products and calculating the price of products and services...
    For which customer and registration by which user
    """
    
    store =  models.ForeignKey(
     Store,related_name='service',on_delete=models.CASCADE,verbose_name=_('فروشگاه ')
    )
    costumer = models.ForeignKey(
        Costumer,related_name='service',on_delete=models.CASCADE,verbose_name=_('مشتری')
        )
    sold_by = models.ForeignKey(  
        User,related_name='sold_by',on_delete=models.CASCADE,verbose_name=_('کاربر ثبت کننده')
    )
    car_model = models.CharField(
        max_length=120,null=True,blank=True,verbose_name=_('مدل ماشین')
        )
    car_km = models.FloatField(
        max_length=120,null=True,blank=True,verbose_name=_('کیلومتر')
    )
    next_appointment = models.DateField(
        null=True, blank=True, verbose_name=_('تاریخ نوبت بعدی')
        )
    product = models.ManyToManyField(
        Product,related_name='service',on_delete=models.CASCADE,verbose_name=_('محصولات')
    )
    quantity = models.IntegerField(
        null=True,blank=True,verbose_name=_('تعداد محصول')
        )
    product_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت مجموع محصولات')
    )
    service_price = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت سرویس ')
        )
    amount_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت کل')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ خدمت')
        )
    
    """
    Validation of latitude and longitude fields
    """
    def clean(self):
    
        if self.latitude is not None and (self.latitude < -90 or self.latitude > 90):
            raise ValidationError({'latitude': _('عرض جغرافیایی باید بین -90 تا 90 باشد.')})
        
       
        if self.longitude is not None and (self.longitude < -180 or self.longitude > 180):
            raise ValidationError({'longitude': _('طول جغرافیایی باید بین -180 تا 180 باشد.')})
    
    
    class Meta:
        verbose_name= _('خدمت')
        verbose_name_plural = _('خدمات')
        ordering = ['-created_at']
        
        
    
class Invoice(models.Model):
    
    """
    Register and record the invoices made with
    the date of registration and for which customer and registration by which user
    """
    service = models.ForeignKey(
        Services,related_name='invoice',on_delete=models.CASCADE,verbose_name=_('خدمات ')
        )
    invoice_number = models.IntegerField(
        verbose_name=_('شماره فاکتور ')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ فاکتور')
        )
    nots = models.TextField(
       null=True,blank=True, verbose_name=_('توضیحات اختیاری')
    )
    costumer = models.ForeignKey(
        Costumer,related_name='costumer',on_delete=models.CASCADE,verbose_name=_('مشتری')
        )
    sold_by = models.ForeignKey(
        User,related_name='sold_by',on_delete=models.CASCADE,verbose_name=_('کاربر ثبت کننده')
    )
    
    class Meta:
        verbose_name= _('صورتحساب')
        verbose_name_plural = _('فاکتور ها')
        ordering = ['-created_at']
    