from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import post_save

class UserType(models.IntegerChoices):
    """
    Define user modes
    """
    superuser = 1, _("superuser")
    admin = 2, _("admin")
    limited_admin = 3,_("limited_admin")
    
    
class UserManager(BaseUserManager):
    
    def create_user(self, phone,password,**extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError("شماره تلفن الزامی است")

        user = self.model(
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,password,**extra_fields):
        """
        Create and save a SuperUser with the given phone and password
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("type", UserType.superuser.value)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    
    phone = models.CharField(
        unique=True,verbose_name=_('شماره تلفن'),max_length=15
        )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    is_verified = models.BooleanField(
        default=False
    )
    type = models.IntegerField(
        choices=UserType.choices,default=UserType.admin.value,verbose_name= _('نقش کاربر')
    )
    created_dete = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد ')
    )
    update_date = models.DateTimeField(
      verbose_name= _(' تاریخ بروز رسانی'),auto_now=True
    )
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'مدیریت کاربران '
    
    
    def __str__(self):
        return self.phone


class Profile (models.Model):
    user = models.OneToOneField(
        'User',on_delete=models.CASCADE,related_name='user_profile'
        )
    first_name = models.CharField(
        max_length=50, verbose_name= _('نام ')
        )
    last_name = models.CharField(
        max_length=50, verbose_name= _(' نام خانوداگی ')
        )
    email = models.EmailField(
        verbose_name=_('ایمیل'),null=True,blank=True
        )
    image = models.ImageField(
        upload_to="profile",null=True, blank=True,verbose_name= _('تصویر پروفایل')
    )
    created_dete = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ایجاد '),
    )
    update_date = models.DateTimeField(
        auto_now=True,verbose_name= _(' تاریخ بروز رسانی')
    )
    
    def get_fullname(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return "کاربر جدید"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'مدیریت پروفایل ها '
    
@receiver(post_save,sender=User)
def cerated_profile(sender,instance,created,**kwargs):
    if created and  instance.type == UserType.limited_admin.value:
        Profile.objects.create(user=instance)
        
    
   
class Otp(models.Model):
    """
    Authentication related model
    with token creation feature
    """
    token = models.CharField(
        max_length=200, null=True, verbose_name='توکن'
        )
    phone = models.CharField(
    max_length=11,
    validators=[RegexValidator(regex=r'^09\d{9}$', message='شماره تلفن باید با 09 شروع شده و 11 رقم باشد')],
    verbose_name='شماره تلفن'
        )

    code = models.SmallIntegerField(
        verbose_name='کد یکبار مصرف'
        )
    code_expiry = models.DateTimeField(
        verbose_name='تاریخ انقضای کد',default=timezone.now() + timedelta(minutes=2),
        )
    
    def is_expired(self):
        return timezone.now() > self.code_expiry + timezone.timedelta(minutes=2)
    
    def __str__(self):
        return f"{self.code}"
    
    class  Meta:
        verbose_name = 'رمز یکبار مصرف'
        verbose_name_plural = ' احراز هویت Otp'