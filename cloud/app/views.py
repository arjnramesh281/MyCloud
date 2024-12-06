from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def log(req):
    if 'user' in req.session:
        return redirect(home)
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        print(username+password)
        data=authenticate(username=username,password=password)
        if data:
            login(req,data)
            req.session['user']=username
            return redirect(home)
        else:
            messages.warning(req, " Invalid username or password.")
            return redirect(log)
    else:
        return render(req,'login.html')


def reg(req):
    if req.method=='POST':
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=username,email=email,username=email,password=password)
            data.save()
        except:
            messages.warning(req, " This Email Already In Use.")
            return redirect(reg)
        return redirect(log)
    else:
     return render(req,'user/register.html')





def home(req):
    return render(req,'user/home.html')



