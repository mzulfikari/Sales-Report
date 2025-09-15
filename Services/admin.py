from django.contrib import admin
from . models import Services,Invoice
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    
    list_display = (
        "store",
        "customer_phone",
        "sold_by",
        "car",
        "show_image",
        "amount_total",
        "get_created_jalali",)
    
    search_fields=(
        "created_at",
        )
    
    list_filter = (
            "created_at",
            )
    
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "customer_phone",
        "invoice_number",
        "sold_by",
        "get_created_jalali",
        )
    
    search_fields=(
        "customer_phone",
        "invoice_number",
        )
    
    list_filter = (
            "created_at",
            )
    
    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')

    