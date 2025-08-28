from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Otp
from .forms import Verfiy


admin.site.site_header = 'پنل مدیریت سرویس خودرو'


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for user management with add and change forms plus password
    """
    model = User
    list_display = ("id","phone_display","is_superuser","is_active","is_verified")
    list_filter = ("phone", "is_superuser",)
    ordering = ("phone",)
    
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("phone", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions","type"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "type"
                ),
            },
        ),
    )
    
    def phone_display(self, obj):
     return obj.phone or "—"
    phone_display.short_description = "شماره تلفن"
    phone_display.admin_order_field = "phone"

class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ("id","user", "first_name","last_name","get_phone")
    searching_fields = ("user","first_name","last_name",)
    
    @admin.display(description='شماره تلفن')
    def get_phone(self, obj):
        return obj.user.phone
    

@admin.register(Otp)
class OTPAdmin(admin.ModelAdmin):
    list_display = ("phone", "code",)

admin.site.register(Profile,CustomProfileAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
