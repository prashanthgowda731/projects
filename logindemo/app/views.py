from django.shortcuts import render
from app.form import *

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    if request.session.get('username'):
        user=request.session.get('username')
        return render(request,"home.html",context={"username":user})
    return render(request,"home.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def l(request):
    return HttpResponse("<h1>hai</h1>")

def register(request):
    registered=False
    if request.method=="POST" and request.FILES:
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST,request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save(commit=False)
            user.set_password(userform.cleaned_data['password'])
            user.save()

            profile=profileform.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
    userform=UserForm()
    profileform=ProfileForm()
    d={'registered':registered,'userform':userform,'profileform':profileform}
    return render(request,'register.html',context=d)

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Not a Active User or Invalid username and password")
    return render(request,'user_login.html',context={})
