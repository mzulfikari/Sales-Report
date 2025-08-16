from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login, logout
from .forms import LoginCustomer,VerfiyCustomer
from uuid import uuid4
from random import randint
from django.urls import reverse
from .models import Otp

class UserRegister(View):
    """User login through phone number and email"""

    def get (self,request):
        form = VerfiyCustomer()
        return render (request,'accounts/customer/verfiy.html',
         {'form':form})

    def post(self,request):
        phone = request.POST.get('phone')
        form = VerfiyCustomer(request.POST)
        if form.is_valid():
          
            valid = form.cleaned_data
            randcode = randint(1000,9999)
            #دریافت رمز یکبار مصرف
            # sms_api.verification({
            #     'receptor':valid["phone"],'type':'1','template':'randcode','param1':randcode
            # })
            token = str(uuid4())
            Otp.objects.create(phone=valid['phone'],
                code=randcode,
                token=token
                )
            return redirect(reverse('account:Verify') + f'?token={token}')
        else:
                form.add_error('phone', "اطلاعات وارد شده صحیح نمی باشد ")
        return render(request,"accounts/customer/verfiy.html",{'form':form,'phone': phone})


class CutomerLogin(View):
    """
    To check customer information and validate contact number
    """
    def get(self,request):
        form = LoginCustomer()
        return render(
            request,'accounts/customer/login.html',{'form':form}
            )
        
    def post(self,request):
        form = LoginCustomer(request.POST)
        if form.is_valid():
            valid = form.clean_data 
            login_user = authenticate(phone=valid['phone'])
            if login_user is not None:
             login(request,login_user)
             return redirect('')
        else:
            form.add_error("phone","اطلاعات وارد شده صحیح نمی باشد")
            return render(
                request,'accounts/login.html',{'form':form}
                )   

# class Verify(TemplateView):
    
#     template_name = 'accounts/customer/verfiy.html'