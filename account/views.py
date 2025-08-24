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
        customer_phone = request.session.get('customer_phone')
        context= {
        'form': form ,
        'customer_phone': customer_phone
        }
        return render(request, 'accounts/verfiy.html',context)

    def post(self,request):
        customer_phone = request.session.get('customer_phone')
        token = request.GET.get('token')
        form = Verfiy(request.POST)
        context= {
            'form': form ,
            'customer_phone': customer_phone
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
