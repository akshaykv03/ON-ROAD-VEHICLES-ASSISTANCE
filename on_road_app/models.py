from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Mechanic(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Bookings(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    mechanic=models.ForeignKey(Mechanic,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    lat=models.CharField(max_length=50)
    lon=models.CharField(max_length=50)
    estReachDist=models.CharField(max_length=100,default="-")    
    estReachTime=models.CharField(max_length=100,default="-")   
    status=models.CharField(max_length=50,default="Pending")
    rate=models.CharField(max_length=50) 
    desc=models.CharField(max_length=50) 
    review=models.BooleanField(default=False)
    
    

class SOS(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    lat=models.CharField(max_length=50)
    lon=models.CharField(max_length=50)
    msg=models.CharField(max_length=150)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)


class Fire(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    lat=models.CharField(max_length=50)
    lon=models.CharField(max_length=50)
    msg=models.CharField(max_length=150)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)


class Feedback(models.Model):
    date=models.DateTimeField(auto_now_add=True)   
    booking=models.ForeignKey(Bookings,on_delete=models.CASCADE,null=True)
    feedback=models.CharField(max_length=300,null=True,default="-")
     




