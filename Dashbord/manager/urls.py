from django.urls import path,include
from . import views

app_name = "manager"

urlpatterns = [  
    path('dashbord/',views.AdminDashbordViews.as_view(),name="dashbordviews"),
    
  
]
