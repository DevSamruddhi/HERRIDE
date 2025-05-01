from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from HERRIDE.models import  CustomUser,Driver
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html') 
def services(request):
    return render(request,'services.html')
def jobs(request):
    return render(request,'jobs.html')
def userlogin(request):
    if request.method=="POST":
        ue=request.POST.get("uemail")
        upwd=request.POST.get("upwd")
        user=authenticate(request,username=ue,password=upwd)
        if user is not None:
            login(request,user)
            print("Login Successfully")
            return redirect('map2')
        else:
            print("Invalid Credentials!") 
            return render(request,"user_login.html",{'error':'Invalid Credentials'})
    return render(request,'user_login.html')
def driverlogin(request):
    if request.method=="POST":
        de=request.POST.get("demail")
        dpwd=request.POST.get("dpwd")
        user=authenticate(request,username=de,password=dpwd)
        if user is not None:
            login(request,user)
            print("Login Successfully")
            return redirect('map2')
        else:
            print("Invalid Credentials!") 
            return render(request,"driver_login.html",{'error':'Invalid Credentials'})
    return render(request,'driver_login.html')
def registration(request):
    if request.method=="POST":
        role=request.POST.get("role")
        checkbox=request.POST.get("checkbox")
        if not checkbox:
                return render(request,'registration.html',{'error':"Please accept Terms and Conditions"})
        if role=="User":
            un=request.POST.get("uname")
            uphn=request.POST.get("uphn")
            ue=request.POST.get("uemail")
            upwd=request.POST.get("upwd")
            if CustomUser.objects.filter(userame=uphn).exists():
                return render(request,'registration.html',{'error':'Phone No exists'})
            else:
                uobj=CustomUser.objects.create(uphn=uphn,uname=un,uemail=ue,upwd=upwd) 
                uobj.save()
                print("Registered Succsessfully")
                return redirect("ulogin")
        elif role=="Driver":
            dn=request.POST.get("dname")
            dphn=request.POST.get("dphn")
            de=request.POST.get("demail")
            dpwd=request.POST.get("dpwd")
            if Driver.objects.filter(dphn=dphn).exists():
                return render(request,'registration.html',{'error':'Phone No exists'})
            else:
                dobj=Driver.objects.create(dphn=dphn,dname=dn,demail=de,dpwd=dpwd)
                dobj.set_password(dpwd) 
                dobj.save()
                return redirect("dlogin")
    return render(request, 'registration.html')
def map2(request):
    return render(request,'map2.html')
def tandc(request):
    return render(request,'tandc.html')