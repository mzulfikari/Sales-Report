from django.urls import path
from .import views

app_name="account"

urlpatterns = [
   path('login/customer',views.CutomerLogin.as_view(),name='Login-user'),
   path('verify/customer',views.UserRegister.as_view(), name='Verify'),
]