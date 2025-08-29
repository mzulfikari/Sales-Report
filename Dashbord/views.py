from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from account.models import UserType

class DashbordViews(LoginRequiredMixin,View):
    """
    Checking the user's typing to enter the dashboard related to user access
    """
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == UserType.admin.value:
                redirect(reverse_lazy('#'))
            elif request.user.type == UserType.limited_admin.value:
                redirect(reverse_lazy('#')) 
        else:
            redirect(reverse_lazy('account:'))
        return super().dispatch(request, *args, **kwargs)
        
    
class ProfileShopViews(TemplateView):
    
    template_name = 'dashbord/manager/profile_shop.html'