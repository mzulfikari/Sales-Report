from django.urls import path,include
from . import views

app_name = "Dashbord"

urlpatterns = [  
    path('dashbord',views.DashbordViews.as_view(),name="dashbord"),
    
    #include manager urls
    path("manager/", include(("Dashbord.manager.urls", "manager"), namespace="manager")),

    
    # #include admin_limit urls
    # path("admin_limit/",include('Dashbord.admin_limit.urls')),
    
    # #include costumer urls
    # path("costumer/",include('Dashbord.costumer.urls')),

]
