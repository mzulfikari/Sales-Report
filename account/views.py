from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login, logout
from .forms import LoginCustomer,VerfiyCustomer
from uuid import uuid4
from random import randint
from django.urls import reverse
from .models import Otp

class CutomerVerfiy(View):
    """
    Customer login through phone 
    """
    template_name = "accounts/customer/login.html"
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        phone = request.POST.get("phone")
        try:
            service = Services.objects.get(phone=phone)
            # تولید OTP
            otp = randint(length=4, allowed_chars='0123456789')
            request.session['customer_otp'] = otp
            request.session['customer_id'] = service.id
            # در حالت واقعی این otp باید SMS شود
            print(f"OTP برای تست: {otp}")
            return redirect('customer_verify_otp')
        except Services.DoesNotExist:
            messages.error(request, "شماره تلفن معتبر نیست")
            return render(request, self.template_name)

class CutomeVerfiyCode(View):
    """
    To check customer information and validate contact number
    """
    def get(self,request):
        form = LoginCustomer()
        return render(
            request,'accounts/customer/verfiy.html',{'form':form}
            )
        
    def post(self,request):
        form = LoginCustomer(request.POST)
        if form.is_valid():
            valid = form.cleaned_data
            login_user = authenticate(phone=valid['phone'])
            if login_user is not None:
             login(request,login_user)
             return redirect('')
        else:
            form.add_error("phone","اطلاعات وارد شده صحیح نمی باشد")
            return render(
                request,'accounts/customer/verfiy.html',{'form':form}
                )   

# class Verify(TemplateView):
    
#     template_name = 'accounts/customer/verfiy.html'