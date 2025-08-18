from django.urls import path
from .import views

app_name="account"

urlpatterns = [
   path('customer/verfiy',views.CutomerVerfiy.as_view(),name='cutomerverfiy'),
   path('verify/code',views.CutomerVerfiyCode.as_view(), name='verifycode'),
]