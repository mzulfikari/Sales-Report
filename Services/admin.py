from django.contrib import admin
from . models import Services,Store
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Services)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = (
        "store",
        "sold_by",
        "car",
        "next_km",
        "get_created_jalali",
        "show_image",
        "amount_total",)
    
    search_fields=(
        "get_created_jalali",
        )
    
    list_filter = (
            "store",
            "created_at",
            )
    
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    
    list_display = (
        "title",
        "manager",
        "image",
        "phone",
        "show_image",
        "get_created_jalali",)
    
    search_fields=(
        "get_created_jalali",
        )
    
    list_filter = (
            "title",
            )
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')
