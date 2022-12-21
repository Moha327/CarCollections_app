from django.shortcuts import render,HttpResponse,redirect,get_object_or_404 
from . import models
from django.http import HttpResponse
from .models import Profile,Car
from django.contrib import messages
from django.http import Http404
import bcrypt
from django.utils import timezone
def index(request):
    return  render(request,"index.html")
def index2(request):
    return  render(request,"create-profile.html")
def success(request):
    c={
        'a':models.count_cars(),
        'b':models.some_cardetails(),
        'c':models.show_profile2()
    }
    return render(request,"catalogue.html",c)
    
def createpage(request):
        errors = Profile.objects.validator(request.POST)
        a=Profile(request.POST,request.FILES)
        if a :
            if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/profile')
            else:
                username=request.POST["uname"]
                email=request.POST["el"]
                age=request.POST["ae"]
                password=request.POST["paswd"]
                firstname=request.POST.get("fname",False)
                lastname=request.POST.get("lname",False)
                
                profilepicture=request.FILES.get('ppicture',False)
                
                models.create_profile(username,email,age,password,firstname,lastname,profilepicture)
                return redirect('/catalogue')      
        else:
            return HttpResponse('ldclpcldpcldpc') 
def createcar(request):
        errors = Car.objects.validator2(request.POST)
        if request.method=="POST" :
            if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request, value)
                    return redirect('/car/add')
            else:
                    type=request.POST.get("typ",False)
                    model=request.POST.get("mdl",False)
                    year=request.POST.get("yr",False)
                    imageurl=request.POST.get("iurl",False)
                    price=request.POST.get("prce",False)
                    user=request.POST.get("us",False)
                    
                    if year=='':
                        year=None
                    if price=='':
                        price=None
                    models.create_car(type,model,year,imageurl,price,user)
                    
                    return redirect('/catalogue')            
        else:
            return HttpResponse('ldclpcldpcldpc') 
def updateprofile(request):
        a=Profile(request.POST,request.FILES)
        if a:
                username=request.POST.get("uname", False)
                age=request.POST.get("ae", False)
                email=request.POST.get("el", False)
                firstname=request.POST.get("fname", False)
                lastname=request.POST.get("lname", False)                
                password=request.POST.get("paswd", False)
                profilepicture=request.FILES.get('ppicture',False)
                if 'ppicture' in request.session:
                    profilepicture=request.session['ppicture2']
                models.update_profiledetails(username,age,email,firstname,lastname,password,profilepicture)
                return redirect('/profile/details')
def index4(request):
    return  render(request,"create-car.html")
def index5(request):
    context={
            'b':models.show_car(),
            'c':models.show_profile2(),
            'd':models.sumprice(),
            'e':models.show_profile2()       
    }
    return  render(request,"profile-details.html",context)
def index6(request,profileid):
    context={
          'e':models.display_fav_books(profileid),
          "categoryName": profileid,
          'c':models.show_profile2()
    }
    return  render(request,"profile-edit.html",context)
def index7(request,profileid):
    context={
          'e':models.display_fav_books(profileid),
          "categoryName": profileid,
          'c':models.show_profile2()
    }
    return render(request,"update.html",context) 
def deleteprofile(request):
    context={
        'o':models.delete_profile()
    }
    return render(request,'Delete-profile.html',context)
def deletindex(request):
    return render(request,'Delete-profile.html')
def index8(request,carid):
        return render(request,'car-details.html',context={'k':models.cardetails(carid),'Num':carid,'a':models.count_cars(),
        'b':models.some_cardetails(),
        'c':models.show_profile2()})
def index9(request,carid):
        return render(request,'car-edit.html',context={'k':models.cardetails(carid),'Num':carid,'a':models.count_cars(),
        'b':models.some_cardetails(),
        'c':models.show_profile2()})
def updatecar(request,carid):
    
    if request.method=='POST' :
                carid=carid
                type=request.POST.get("typ", False)
                model=request.POST.get("mdl", False)
                year=request.POST.get("yr",False)
                imageurl=request.POST.get("iurl",False)
                price=request.POST.get("prce",False)
                if year=='':
                        year=None
                if price=='':
                        price=None
                models.update_cardetails(carid,type,model,year,imageurl,price)
                return redirect('/catalogue')
def index10(request,carid):
        return render(request,'car-delete.html',context={'k':models.cardetails(carid),'Num':carid,'d':models.delete_car(carid),'c':models.show_profile2()})