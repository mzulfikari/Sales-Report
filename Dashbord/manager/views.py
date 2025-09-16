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
    
    def post(self,request):
        errors = []
        form = InformationCar(request.POST,request.FILES)
        if form.is_valid():
              infocar = form.save(commit=False)
              infocar.plaque = form.cleaned_data.get("plaque")
              infocar.sold_by = request.user
              infocar.store = request.user.managed_stores.get()
              infocar.save()  
              return  redirect("Dashboard:manager:ServicesAdd", car_id=infocar.id)
        else:
             for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(error)   
                    
             return render (request,'dashbord/manager/service/info_car.html',{
                'form':form,
                'errors': errors
                })


class InvoiceViews(TemplateView):
    
    template_name = 'dashbord/manager/invoice/invoice.html'
    
    
class ServicesAdd(TemplateView):
    
    template_name = 'dashbord/manager/service/service_car.html'
    