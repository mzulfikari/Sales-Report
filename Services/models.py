from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _
from Store.models import Store,Product
from account.models import User
from django.utils.html import format_html



class Services(models.Model):
    """
    Implementation of services with the ability to register a store with limited access to the admin
    Connecting to products and calculating the price of products and services...
    For which customer and registration by which user
    """
    COLOR_CHOICES = [
        ('white', 'سفید'),
        ('black', 'مشکی'),
        ('silver', 'نقره‌ای'),
        ('gray', 'خاکستری (ذغالی)'),
        ('blue', 'سرمه‌ای'),
        ('navy', 'آبی'),
        ('red', 'قرمز'),
        ('green', 'سبز (یشمی/زیتونی)'),
        ('beige', 'بژ (طلایی/کرم)'),
    ]
    
    store =  models.ForeignKey(
     Store,related_name='service',on_delete=models.CASCADE,verbose_name=_('فروشگاه ')
    )
    customer_phone = models.CharField(
        max_length=15,verbose_name=_('شماره تماس مشتری'),null=True,blank=True
        )
    sold_by = models.ForeignKey(  
        User,related_name='services_sold',on_delete=models.CASCADE,verbose_name=_('کاربر ثبت کننده')
    )
    car = models.CharField(
        max_length=120,null=True,blank=True,verbose_name=_('خودرو ')
        )
    car_model = models.CharField(
        max_length=120,null=True,blank=True,verbose_name=_('مدل خودرو ')
    )
    color = models.CharField(
        choices=COLOR_CHOICES,max_length=40,null=True,blank=True,verbose_name=_('رنگ خودرو')
        )
    current_km = models.FloatField(
        max_length=120,null=True,blank=True,verbose_name=_(' کیلومتر فعلی')
    )
    next_km= models.CharField(
      max_length=120,null=True, blank=True, verbose_name=_('تاریخ نوبت بعدی')
        )
    product = models.ManyToManyField(
        Product,related_name='service',verbose_name=_('محصولات')
    )
    quantity = models.IntegerField(
        null=True,blank=True,verbose_name=_('تعداد محصول')
        )
    product_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت مجموع محصولات'),null=False,default=0
    )
    service_price = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت سرویس '),null=False,default=0
        )
    amount_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت کل'),null=False,default=0
    )
    plaque = models.CharField(
      max_length=10, null=True,blank=True,verbose_name=_('شماره پلاک')
        ) 
    image_plaque = models.ImageField(
        null=True,blank=True,verbose_name=_('تصویر پلاک')
    )
    image_km =models.ImageField(
        null=True,blank=True,verbose_name=_('تصویر کیلومتر ')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ خدمت')
    )
    
    def show_image(self):  
     if self.image_plaque:
       return format_html(f'<img src="{self.image_plaque.url}" width="78 px" height="50" />')
     return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصویر پلاک"
    
    
    def __str__(self):
       return self.customer_phone


    class Meta:
        verbose_name= _('خدمت')
        verbose_name_plural = _('سرویس ها')
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
    customer_phone = models.ForeignKey(
        'Services',related_name='costumer',on_delete=models.CASCADE,verbose_name=_('شماره تماس مشتری'),null=True,blank=True
        )
    sold_by = models.ForeignKey(
        User,related_name='invoices_sold',on_delete=models.CASCADE,verbose_name=_('کاربر ثبت کننده')
    )
    
    class Meta:
        verbose_name= _('صورتحساب')
        verbose_name_plural = _('فاکتور ها')
        ordering = ['-created_at']
    
    
