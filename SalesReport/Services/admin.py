from django.contrib import admin
from .models import Product
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = (
        "store",
        "title",
        "brand",
        "price",
        "get_created_jalali",
        "show_image",)

    list_editable=(
        "price",
        )
    search_fields=(
        "title",
        )
    list_filter = (
            "category",
            "inventory",
            "created",
            )
    
    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y')
