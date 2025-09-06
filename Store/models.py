from django.db import models
from django.utils.translation import gettext as _
from account.models import User
from django.utils.html import format_html


class Store (models.Model):
    """
    To register the store by superuser and by admin
    """
    title = models.CharField(
        max_length=60,verbose_name=_('عنوان فروشگاه')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
    )
    phone = models.CharField(
        max_length=15,verbose_name=_('شماره تماس همراه')
        )
    phone_2 = models.CharField(
        max_length=15,verbose_name=_('شماره تماس ثابت')
        )
    address = models.TextField(
        verbose_name=_('آدرس کامل'),null=True,blank=True
    )
    manager = models.ForeignKey(
        User, on_delete=models.CASCADE,verbose_name=_('ادمین فروشگاه'),related_name='managed_stores'
        )
    location_link = models.CharField(
        max_length=250, null=True, blank=True,verbose_name=_('موقعیت/لوکشین')
        )
    is_active = models.BooleanField(
        default=True,verbose_name=_('فعال/غیرفعال')
    )
    image = models.ImageField(
        null=True,blank=True,verbose_name=_('تصویر فروشگاه')
    )
    store_service = models.ManyToManyField(
        'StoreServices',related_name='store_service',verbose_name=_('خدمات فروشگاه'),blank=True
    )
    
    
    def show_image(self):
        """To display images in the management panel"""
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="78 px" height="50" />')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصاویر"
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name= _('فروشگاه')
        verbose_name_plural = _('فروشگاه ها')
        ordering = ['-created_at']
    

class StoreServices(models.Model):
    """ 
    Categories with subcategory context
    """
    title = models.CharField(
        max_length=80,verbose_name=_('عنوان خدمت')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,related_name='children',verbose_name=_('زیر دسته')
        )
    
    def __str__(self):
        return f"{self.title}"
    
    
    class Meta:
        verbose_name= _('نوع خدمت')
        verbose_name_plural = _('خدمات ارائه شده')
        ordering = ['created_at']
    
class Product(models.Model):
    """
    Product details of each store based on admin access
    """
    title = models.CharField(
        max_length=80,verbose_name=_('عنوان محصول')
        )
    store_service = models.ManyToManyField(
        StoreServices, related_name='service_product',verbose_name=_('عنوان خدمت فروشگاه'),blank=True
    )
    brand = models.CharField(
        max_length=100,verbose_name=_('نام برند محصول '),null=True,blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
        )
    image = models.ImageField(
        upload_to='media/Store/Product',verbose_name=_('تصویر'),null=True,blank=True
    )
    
    def __str__(self):
        return f"{self.title}"
    
    
    def show_image(self):
        """To display images in the management panel"""

        if self.image:
            return format_html(f'<img src="{self.image.url}" width="40 px" height="60" />')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصاویر"


    class Meta:
        verbose_name= _('محصول')
        verbose_name_plural = _('محصولات')
        ordering = ['-created_at']
        
        
    

