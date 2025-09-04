from django.urls import path,include
from . import views

app_name = "manager"

urlpatterns = [  
    path('dashbord/',views.AdminDashbordViews.as_view(),name="dashbordviews"),
    path('informationcar/add',views.InformationCarAdd.as_view(),name="informationcar_add"),
    path('invoice/export',views.InvoiceViews.as_view(),name="invoice_export"),
    path('service/add',views.ServicesAdd.as_view(),name="ServicesAdd"),
    
]
