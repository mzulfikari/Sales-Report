from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login, logout



class UserLogin(View):
    @staticmethod
    def get (request):
        form = LoginForm()
        return render(request,'login.html',{'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            valid = form.cleaned_data
            login_user = authenticate(username=valid['username'],password=valid['password'])
            if login_user is not None:
                login(request,login_user)
                return redirect('Product:Product_view')
            else:
                form.add_error("username", "اطلاعات وارد شده صحیح نمی باشد ")
        else:
            form.add_error("username","لطفا دوباره بررسی کنید اطلاعات وارد شده صحیح نمی باشد")

        return render(request,'login.html',{'form':form})
    