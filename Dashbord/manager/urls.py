from django.urls import path,include
from . import views

app_name = "manager"

urlpatterns = [  
    path('dashbord/',views.AdminDashbordViews.as_view(),name="dashbordviews"),
    path('service/add',views.ServoiceAdd.as_view(),name="service_add"),
    path('invoice/export',views.InvoiceViews.as_view(),name="invoice_export"),
    
]
