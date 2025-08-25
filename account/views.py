from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login, logout
from .forms import Verfiy
from .models import Otp

                
class VerfiyCode(View):
    """
    To authenticate the entered number and expire
    the one-time code within 2 minutes
    """
    def get(self, request):
        form = Verfiy()
        phone_customer = request.session.get('phone_customer') 
        context= {
        'form': form ,
        'phone_customer': phone_customer
        }
        return render(request, 'accounts/verfiy.html',context)

    def post(self,request):
        phone_customer = request.session.get('phone_customer')
        token = request.GET.get('token')
        form = Verfiy(request.POST)
        context= {
            'form': form ,
            'phone_customer': phone_customer
        }
        
        if form.is_valid():
            valid = form.cleaned_data
            if Otp.objects.filter(code=valid['code'],token=token,).exists():
             otp = Otp.objects.get(token=token)
             if otp.is_expired:
                    form.add_error('code', "کد منقضی شده است")
                    return render(request, 'accounts/verfiy.html', {'form': form})
             return redirect('/')
            otp.delete()
        else:
            form.add_error(None, "اطلاعات وارد شده صحیح نمی باشد ")
           
        return render(request,'accounts/verfiy.html',context)
