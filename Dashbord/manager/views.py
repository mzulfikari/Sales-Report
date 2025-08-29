from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import TemplateView


class AdminDashbordViews(TemplateView):
    
    template_name = 'dashbord/manager/manager.html'