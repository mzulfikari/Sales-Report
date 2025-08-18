from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login, logout
from ..forms import CustomerVerfiy,VerfiyCustomer
from uuid import uuid4
from random import randint
from django.urls import reverse
from ..models import Otp


class CutomerVerfiy(View):
    """
    Customer login phone 
    """
    def get (self,request):
        form = CustomerVerfiy()
        return render (request,'accounts/customer/login.html',{'form':form})
    
    def post(self,request):
        phone = request.POST.get('phone')
        form = CustomerVerfiy(request.POST)
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
            print(f"OTP for admin {phone}: {randcode}")
            return redirect(reverse('account:verifycode') + f'?token={token}')
        return render(request,"accounts/customer/verfiy.html",{'form':form,'phone': phone})


                
class CutomerVerfiyCode(View):
    """
    To authenticate the entered number and expire
    the one-time code within 2 minutes
    """
    def get(self, request):
        form = VerfiyCustomer()
        return render(request, 'accounts/customer/verfiy.html',
            {'form': form })

    def post(self,request):
        token = request.GET.get('token')
        form = VerfiyCustomer(request.POST)
        
        if form.is_valid():
            valid = form.cleaned_data
            if Otp.objects.filter(code=valid['code'],token=token,).exists():
             otp = Otp.objects.get(token=token)
             if otp.is_expired:
                    form.add_error('code', "کد منقضی شده است")
                    return render(request, 'accounts/customer/verfiy.html', {'form': form})
             return redirect('/')
            otp.delete()
        else:
            form.add_error(None, "اطلاعات وارد شده صحیح نمی باشد ")

        return render(request,'accounts/customer/verfiy.html',{'form':form })
