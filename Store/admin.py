from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Store,Product,StoreServices



@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    
    list_display = (
        "title",
        "manager",
        "phone",
        "show_image",
        "get_created_at_jalali",)
    
    search_fields=(
        "get_created_jalali",
        )
    
    list_filter = (
            "title",
            )
    @admin.display(description='تاریخ ارسال', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b  %Y _ %H:%M')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_created_jalali",
        "show_image",)

    search_fields=(
        "title",
        )
    list_filter = (
            "store_service",
            "created_at",
            )
    
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


@admin.register(StoreServices)
class StoreServicesAdmin(admin.ModelAdmin):
    list_display = ("title","get_created_jalali",)
    list_filter = ("created_at",)
    search_fields = ("title",)
    
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')
