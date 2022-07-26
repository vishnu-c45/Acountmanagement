from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    desigination=models.CharField(max_length=150)
    image=models.ImageField(upload_to="image", null=True)
    joining_date=models.DateField()


class leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True)                       
    from_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    to_date= models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
   
class attendence(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    date=models.DateField()
    status=models.CharField(max_length=200)

class task(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    task=models.CharField(max_length=200)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=200)
    file=models.FileField(upload_to="image",null=True)
    
 
