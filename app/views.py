from datetime import datetime
from email import message
from itertools import count
from pyexpat.errors import messages
from turtle import update
from django.shortcuts import render ,redirect
from django.contrib.auth.models import auth,User 
from django.contrib import messages
from .models import *

# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html') 

def adminhome(request):
    count2=User.objects.filter(is_superuser=0).count()
    count3=leave.objects.all().count()
    count4=attendence.objects.all().count()
    return render(request,'adminhome.html',{'count2':count2,'count3':count3,'count4':count4})       

def myprofile(request,pk):
     std=User.objects.get(id=pk)
     return render(request,'myprofile.html',{'std':std})
   

def usercreate(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        uname=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'this user name is already exists!!!')
                return redirect('signup')
            else:
                pro=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    username=uname,
                    password=password,)
                pro.save()
                messages.info(request,'user created successfully')
        else:
            messages.info(request,'password does not match !!!')    
            return redirect('signup')     
    return render(request,'signup.html')


def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        request.session["uid"]=user.id
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                # return render(request,'adminhome.html')
                return redirect('adminhome')
            else:
                auth.login(request,user)
                messages.info(request,f'welcome {username}')   
                return render(request,'home.html') 
        else:
            messages.info(request,'invalid username and password !!!')      
            return redirect('login')  
    return render(request,'login.html')   


def leaveapply(request,pk):
    std=User.objects.get(id=pk)
    return render(request,'leaveapply.html',{'std':std}) 


def user_apply_leave(request,pk):
    std=User.objects.get(id=pk)

    if request.method == "POST":
        mem=leave()
        mem.from_date = request.POST.get('from')
        mem.to_date = request.POST.get('to')
        mem.leave_status = request.POST.get('haful')
        mem.reason = request.POST.get('reason')
        mem.status = "pending"
        mem.user_id=std.id
        mem.save()
            
    return render(request,'leaveapply.html',) 


def viewleave(request,pk):
    std=leave.objects.filter(user_id=pk)
    return render(request,'viewleave.html',{'std':std})


def adminleave(request):
    std=leave.objects.all()
    return render(request,'admin.html',{'std':std}) 

def Admin_reject(request,id):
    pro_sts = leave.objects.filter(id=id).update(status ='rejected')
    return redirect('adminleave')
   


def Admin_approve(request,id):
    al = leave.objects.filter(id=id).update(status ='approved')
    return redirect('adminleave')  


def viewuser(request):
    std=User.objects.filter(is_superuser=0)
    return render(request,'viewusers.html',{'std':std}) 


def add2(request,pk):
    mem=User.objects.get(id=pk)
    std=attendence()
    # std.date=request.POST.get('date')
    std.status="ABSENT"
    std.date=datetime.now()
    std.user_id=mem.id
    std.save()
    return redirect('atten') 
    
def add(request,pk):
    mem=User.objects.get(id=pk)
    std=attendence()
    # std.date=request.POST.get('date')
    std.status="PRESENT"
    std.date=datetime.now()
    std.user_id=mem.id
    std.save()
    return redirect('atten') 
    
def atten(request):
    std=attendence.objects.all()
    return render(request,'viewattendence.html',{'std':std})

def viewatten(request,pk):
    std=attendence.objects.filter(user_id=pk)
    return render(request,'userattendence.html',{'std':std})  

def addatten(request):
    std=User.objects.filter(is_superuser=0)
    return render(request,'add_attendence.html',{'std':std})
    


def addtask(request):
    std=User.objects.filter(is_superuser=0)
    return render(request,'update.html',{'std':std})



# def taskk(request):
#     if request.method=='POST':
#         mem=task()
#         mem.task=request.POST.get('task1')
#         mem.start_date=request.POST.get('sdate')
#         mem.end_date=request.POST.get('edate')
#         mem.status="pending"
#         mem.save()
#         return redirect('addtask')
#     return render(request,'update.html')  
def taskk(request):
    if request.method=='POST':
        tas=request.POST['task1']  
        sda=request.POST['sdate']
        eda=request.POST['edate']
        sta="pending"
        se=request.POST['se1']
        cou=User.objects.get(id=se)
        std=task(task=tas,
                start_date=sda,
                end_date=eda,
                status=sta,
                user=cou)
        std.save()   
        return redirect('addtask')
    return render(request,'update.html')           


def viewtask(request,pk):
    std=task.objects.filter(user_id=pk)
    return render(request,'viewtask.html',{'std':std})


def click_up(request,pk,k):
    std=User.objects.get(id=k)
    k=task.objects.get(id=pk)
    return render(request,'uploadtask.html',{'std':std ,'u':k})


def uploadtask(request,pk,k):
    if request.method=='POST':
        cm=User.objects.get(id=k)
        std=task(id=pk)
        std.task=request.POST.get('task')
        std.start_date=request.POST.get('sdate')
        std.end_date=request.POST.get('edate')
        std.file=request.FILES.get('file')
        std.status="completed ✓"
        std.user_id=cm.id
        std.save()
        return redirect('home')
    #return render(request,'viewtask.html')    

def deleteuser(request,pk):
    std=User.objects.get(id=pk)
    std=attendence.objects.get(id=pk)
    std=task.objects.get(id=pk)
    std.delete()
    return redirect('viewuser')

# def deletetask(request,pk):
#     std=task.objects.get(id=pk)  
#     std.delete()
#     return redirect('admin_viewtask')




def admin_viewtask(request):
    std=task.objects.all()
    return render(request,'admintask.html',{'std':std})



def updateprofie(request,pk):
    std=User.objects.get(id=pk)
    return render(request,'updateprofile.html',{'std':std})

def upda(request,pk):  
    if request.method=='POST':
        std=User.objects.get(id=pk)
        std.first_name=request.POST.get('firstname')
        std.last_name=request.POST.get('lastname')
        std.email=request.POST.get('email')
        std.username=request.POST.get('username')
        
        std.save()
        return redirect('home')
    



               
                       


