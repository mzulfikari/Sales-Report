from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models.signals import post_save



class UserType(models.IntegerChoices):
    """
    Define user modes
    """
    customer = 1, _("customer")
    Limited_admin = 2,_("Limited_admin")
    admin = 3, _("admin")
    superuser = 4, _("superuser")


class UserManager(BaseUserManager):
    
    def create_user(self, phone,password,**extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError("شماره تلفن الزامی است")

        user = self.model(
            phone=phone,
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


class admin(AbstractBaseUser,PermissionsMixin):
    
    frist_name = models.CharField(
        max_length=30,verbose_name=_('نام')
    )
    last_name = models.CharField(
        max_length=30,verbose_name=_('نام خانوداگی')
        )
    email = models.EmailField(
        max_length=255,verbose_name=_('آدرس ایمیل ادمین')
    )
    phone = models.CharField(
        unique=True,max_length=15,verbose_name=_('شماره تلفن ادمین')
        )
    is_active = models.BooleanField(
        default=True,verbose_name=_('وضعیت فعالیت')
    )
    is_admin = models.BooleanField(
        default=False,verbose_name=_('وضعیت ادمین')
        )
    cerated_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ثبت')
    )
    type = models.IntegerField(
        choices=UserType.choices, default=UserType.admin.value)
    
    objects = UserManager()

    USERNAME_FIELD = "phone"
    
    
    def __str__(self):
        return  f"{self.frist_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
 
 
class Costumer(models.Model):
    """ 
    Customer authentication based on phone number
    """
    phone = name = models.CharField(
        max_length=15
        )
    created_at = models.DateTimeField(
        auto_now_add=True,verbose_name=_('تاریخ ثبت ')
    )
    
    
    class Meta:
        verbose_name = 'پروفایل مشتری'
        