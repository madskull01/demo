from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import Emp,Register,Login
from .forms import EmpForm,RegisterForm,LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate



# Create your views here.
def home(request):
  return render(request,'home.html')

class MyTestClass(View):
    def get(self,request):
        form=EmpForm()
        d={'form':form}
        return render (request,'test.html',d)

    def post(self,request):
        form=EmpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show/')

def show(request):
        data=Emp.objects.all()
        d={'data':data}
        return render(request,'empshow.html',d)

def update_data(request,pk):
    sdata=Emp.objects.get(id=pk)
    form=EmpForm(instance=sdata)
    if request.method=='POST':
        form=EmpForm(request.POST,request.FILES,instance=sdata)
        if form.is_valid():
            form.save()
            return redirect('/show/')

    return render(request,'test.html',{'form':form})

def delete_data(request,id):
    form=Emp.objects.get(id=id)
    form.delete()
    return redirect('/show/')

def viewplayer(request,id):
    one_rec=Emp.objects.get(pk=id)
    d={'data':one_rec}
    return render(request,'view.html',d)

def register(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=User.objects.create_user(name,username,password)
            
            user.save()
            return redirect('/login/')
    else:
        form=RegisterForm()
        form2=LoginForm()
        d={'form':form,'form2':form2}
        return render(request,'register.html',d)

def login(request):
    if request.method=='POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            auth_login(request,myuser)
            return redirect('/show/')
        else:
            return redirect('/')
    else:
        form2=LoginForm()
        d={'form2':form2}
        return render(request,'login.html',d)

def logout(request):
    auth_logout(request)
    return redirect('/')