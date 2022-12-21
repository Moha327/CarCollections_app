from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save #add this
from datetime import *
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.utils import timezone
import re
from django.core import validators
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
class ProfileManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData["uname"])<2:
            errors["uname"]="The username must be minimum 2 chars"
        return errors
    
class CarManager(models.Manager):
    def validator2(self,postData):
        errors={}
        if len(postData["iurl"])>2049 and len(postData["iurl"])<1980:
            errors["iurl"]="Year must be between 1980 and 2049"
        return errors
class Profile(models.Model):
    MIN_AGE_VALUE = 18
    MAX_AGE_VALUE = 60
    username = models.CharField(max_length=10,null=False,blank=False)
    email= models.TextField(max_length=100,null=False,blank=False)
    age= models.IntegerField(default=0,validators=(validators.MaxLengthValidator(MAX_AGE_VALUE),validators.MinLengthValidator(MIN_AGE_VALUE)),null=False,blank=False)
    password=models.CharField(max_length=30,null=True,blank=True)
    firstname=models.CharField(max_length=30,null=True,blank=True)
    lastname=models.CharField(max_length=30,null=True,blank=True)
    profilepicture=models.ImageField(upload_to='',null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ProfileManager()

def __str__(self):
    return self.objects   

class Car(models.Model):
   
    type = models.CharField(max_length=10,blank=True,default=1)
    model= models.CharField(max_length=20,null=True)
    year = models.IntegerField( null=True)
    imageurl = models.URLField(null=False)
    user=models.ForeignKey(Profile,related_name="cars",on_delete=models.CASCADE)
    price = models.FloatField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CarManager()
def __str__(self):
    return self.objects  
def create_profile(username,email,age,password,firstname,lastname,profilepicture):
    return Profile.objects.create(username=username,email=email,age=age,password=password,firstname=firstname,lastname=lastname,profilepicture=profilepicture)
def create_car(type,model,year,imageurl,price,user):
    user=Profile.objects.last()
    return Car.objects.create(type=type,model=model,year=year,imageurl=imageurl,price=price,user=user)
def display_fav_books(profileid):
    user=Profile.objects.get(id=profileid)
    return user
def getusername(profileid):
    return Profile.objects.get(id=profileid).username
def getuserage(profileid):
    return Profile.objects.get(id=profileid).age
def getuseremail(profileid):
    return Profile.objects.get(id=profileid).email
def getuserfname(profileid):
    return Profile.objects.get(id=profileid).firstname
def getuserlname(profileid):
    return Profile.objects.get(id=profileid).firstname
def some_cardetails():
    user=Profile.objects.last()
    return Car.objects.filter(user=user)
def show_car():
    return Car.objects.all()
def show_car():
    return Car.objects.all()
def show_profile():
    return Profile.objects.all()
def show_profile2():
    return Profile.objects.last()
def count_cars():
    user=Profile.objects.last()
    return Car.objects.filter(user=user).count()
def get_profile_id(username):
    return Profile.objects.get(username=username).id
def update_profiledetails(username,age,email,firstname,lastname,password,profilepicture):
    a=Profile.objects.last()
    a.username=username
    a.age=age
    a.email=email
    a.firstname=firstname
    a.lastname=lastname
    a.profilepicture=profilepicture
    a.password=password
    a.save()
def update_cardetails(carid,type,model,year,imageurl,price):
    
    b=Car.objects.get(id=carid)
    b.type=type
    b.model=model
    b.year=year
    b.imageurl=imageurl
    b.price=price
    b.save()
def delete_profile():
    a=Profile.objects.last()
    a.delete()
def delete_car(carid):
    a=Car.objects.get(id=carid)
    a.delete()
def check_email(email):
    if len(Profile.objects.filter(email=email))==0:
        return False
    else:
        return True
def myprofile():
    return Profile.objects.last()
def sumprice():
    user=Profile.objects.last()
    return sum([car.price for car in Car.objects.filter(user=user).all()])
def cardetails(carid):
    return Car.objects.get(id=carid) 
def createchoices():
    car=Car.objects.last()
    return Profile.objects.filter(car=car)
