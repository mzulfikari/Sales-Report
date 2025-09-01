from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import TemplateView


class AdminDashbordViews(TemplateView):
    
    template_name = 'dashbord/manager/dashbord/manager.html'
    
class ServoiceAdd(TemplateView):
    
    template_name = 'dashbord/manager/service/add_service.html'
    
class InvoiceViews(TemplateView):
    
    template_name = 'dashbord/manager/invoice/invoice.html'
    
    