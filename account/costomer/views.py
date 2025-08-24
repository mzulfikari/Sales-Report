from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login, logout
from .forms import CustomerVerfiy
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
        phone_customer = request.POST.get('phone_customer')
        form = CustomerVerfiy(request.POST)
        if form.is_valid():
            valid = form.cleaned_data
            randcode = randint(1000,9999)
            #دریافت رمز یکبار مصرف
            # sms_api.verification({
            #     'receptor':valid["phone"],'type':'1','template':'randcode','param1':randcode
            # })
            token = str(uuid4())
            Otp.objects.create(phone=valid['phone_customer'],code=randcode,token=token)
            request.session['phone_customer'] = valid['phone_customer']
            print(f"OTP for {phone_customer}: {randcode}")
            return redirect(reverse('account:verifycode') + f'?token={token}')
        return render(request,"accounts/customer/verfiy.html",{'form':form})

