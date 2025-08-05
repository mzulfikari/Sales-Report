from django.db import models
from django.utils.translation import gettext as _


class Store (models.Model):
    title = models.CharField(
        max_length=60,verbose_name=_('عنوان فروشگاه')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
    )
 

class Category (models.Model):
    title = models.CharField(
        max_length=80,verbose_name=_('عنوان دسته بندی')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='parent',verbose_name=_('زیر دسته')
        )
    
    
class Product(models.Model):
    title = models.CharField(
        max_length=80,verbose_name=_('عنوان محصول')
        )
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category',verbose_name=_('دسته بندی')
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
    
