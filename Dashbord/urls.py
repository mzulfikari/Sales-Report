from django.urls import path
from . import views

app_name = "dashbord"

urlpatterns = [  
    path('',views.IndexViews.as_view(),name="Index"),

]
