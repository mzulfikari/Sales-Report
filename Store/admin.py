from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Store,Product,Category



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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
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
            "created_at",
            )
    
    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","get_created_jalali",)
    list_filter = ("created_at",)
    search_fields = ("title",)
    
    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y')
