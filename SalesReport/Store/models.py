from django.db import models
from django.utils.translation import gettext as _
from account.models import User


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
        max_length=15,verbose_name=_('شماره تلفن')
        )
    address = models.TextField(
        verbose_name=_('آدرس'),null=True,blank=True
    )
    manager = models.ForeignKey(
        User, on_delete=models.CASCADE,verbose_name=_('ادمین فروشگاه'),related_name='managed_stores'
        )
    latitude = models.FloatField(
        verbose_name=_('عرض جغرافیایی'),null=True,blank=True
    )
    longitude = models.FloatField(
        verbose_name=_('طول جغرافیایی'),null=True,blank=True
    )
    is_active = models.BooleanField(
        default=True,verbose_name=_('فعال/غیرفعال')
    )
    
    class Mets:
        verbose_name= _('فروشگاه')
        verbose_name_plural = _('فروشگاه‌ها')
        ordering = ['-created_at']
    

class Category (models.Model):
    """ 
    Categories with subcategory context
    """
    title = models.CharField(
        max_length=80,verbose_name=_('عنوان دسته بندی')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='parent',verbose_name=_('زیر دسته')
        )
    
    class Meta:
        verbose_name= _('دسته بندی ')
        verbose_name_plural = _('دسته بندی ها')
        ordering = ['-created_at']
    

    
    
class Product(models.Model):
    """
    Product details of each store based on admin access
    """
    title = models.CharField(
        max_length=80,verbose_name=_('عنوان محصول')
        )
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='product',verbose_name=_('دسته بندی')
    )
    store = models.ForeignKey(
        Store,on_delete=models.CASCADE, related_name='store',verbose_name=_('فروشگاه')
        )
    brand = models.CharField(
        max_length=100,verbose_name=_('نام برند محصول '),null=True,blank=True
    )
    price = models.DecimalField(
       max_digits=10,decimal_places=0,verbose_name=_('قیمت محصول')
        )
    quantity = models.IntegerField(
        verbose_name=_('تعداد محصول'),null=True,blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
        )
    image = models.ImageField(
        upload_to='media/Store/Product',verbose_name=_('تصویر'),null=True,blank=True
    )
    
    class Meta:
        verbose_name= _('محصول')
        verbose_name_plural = _('محصولات')
        ordering = ['-created_at']
    

