from django.urls import path
from .import views
from .costomer.views import CutomerVerfiy
app_name="account"

urlpatterns = [
   path('customer/verfiy',CutomerVerfiy.as_view(),name='cutomerverfiy'),
   path('verify/code',views.VerfiyCode.as_view(), name='verifycode'),
]