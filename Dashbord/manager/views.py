from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic import TemplateView
from ..forms import InformationCar
from django.contrib.auth.mixins import LoginRequiredMixin

class AdminDashbordViews(TemplateView):
    
    template_name = 'dashbord/manager/dashbord/manager.html'
    
    
class InformationCarAdd(LoginRequiredMixin,View):
    """ 
    view related to the registration of 
    car information and specifications
    """
    def get(self, request):
        form = InformationCar()
        return render (request,'dashbord/manager/service/info_car.html',{'form':form})
    
    def post(self, request):
        user = request.user
        form = InformationCar(request.POST)
        if form.is_valid():
            infocar = form.save(commit=False)
            infocar.sold_by = request.user
            infocar.store = request.user.managed_stores.get()
            infocar.save()  
            return  redirect("Dashboard:manager:ServicesAdd", car_id=infocar.id)
        else:      
            return render (request,'dashbord/manager/service/info_car.html',{'form':form})
    
class InvoiceViews(TemplateView):
    
    template_name = 'dashbord/manager/invoice/invoice.html'
    
    
class ServicesAdd(TemplateView):
    
    template_name = 'dashbord/manager/service/service_car.html'
    