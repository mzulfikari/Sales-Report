from django.db import models
from django.utils.translation import gettext as _
from Store.models import Store,Product
from account.models import Costumer


class Services(models.Model):
    store =  models.ForeignKey(
     Store,related_name='store',on_delete=models.CASCADE,verbose_name=_('فروشگاه ')
        )
    costumer = models.ForeignKey(
        Costumer,related_name='costumer',on_delete=models.CASCADE,verbose_name=_('مشتری')
        )
    sold_by = models.ForeignKey(
        
    )
    car_model = models.CharField(
        max_length=120,null=True,blank=True,verbose_name=_('مدل ماشین')
        )
    car_km = models.FloatField(
        max_length=120,null=True,blank=True,verbose_name=_('کیلومتر')
    )
    product = models.ManyToManyField(
        Product,related_name='product',on_delete=models.CASCADE,verbose_name=_('محصولات')
        )
    quantity = models.IntegerField(
        null=True,blank=True,verbose_name=_('تعداد محصول')
    )
    product_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت مجموع محصولات')
    )
    service_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت مجموع سرویس ')
    )
    amount_total = models.DecimalField(
        max_digits=10,decimal_places=0,verbose_name=_('قیمت کل')
    )


class Invoice(models.Model):
    service = models.ForeignKey(
        Services,related_name='service',on_delete=models.CASCADE,verbose_name=_('خدمات ')
        )
    invoice_number = models.IntegerField(
        verbose_name=_('شماره فاکتور ')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد')
        )
    nots = models.TextField(
       null=True,blank=True, verbose_name=_('توضیحات اختیاری')
       )
    costumer = models.ForeignKey(
        Costumer,related_name='costumer',on_delete=models.CASCADE,verbose_name=_('مشتری')
        )
    sold_by = models.ForeignKey(
        
    )
    