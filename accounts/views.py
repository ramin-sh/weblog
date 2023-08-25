from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import MyForm
from blog.models import *
#..............................
import random

def generate_random_code():
    code = random.randint(100000, 999999)
    return code
random_code = str(generate_random_code())

#..........................
def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            # return HttpResponse('login shodi')
            login(request,user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context ={
                "username":username,
                "errorMessage":"کاربری با این مشخصات یافت نشد."
            }
            return render(request, 'accounts/login.html',context)
    else:
        return render(request, 'accounts/login.html')

@login_required    
def edit_post(request,post_id):
    context ={}
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, request.FILES or None,instance=post)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        context['message'] = "پست جدید ایجاد گردید."
    context['form']= form
    return render(request, "accounts/add_post.html", context)

@login_required  
def add_newpost(request):
    context ={}
    form = PostForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        context['message'] = "پست جدید ایجاد گردید."
    context['form']= form
    return render(request, "accounts/add_post.html", context)




def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/accounts/')


def faramooshi(request):

    

    #send_mail('safafromdjango','from django',settings.EMAIL_HOST_USER,['your mail'])
    #User.objects.get()
    

    if request.method == 'GET':
        
        return render(request,"accounts/code.html")
        
    else:
        if request.POST.get('code') == random_code:
            
            return render(request,'accounts/passwordset.html')
            
        else:
            return HttpResponse('کد وارد شده صحیح نمی باشد')
    #---------------------


def set_pass(request):
    if request.method == 'POST':
        user_password = request.POST.get('pass')
        u = User.objects.get(username=user)
        u.set_password(user_password)
        u.save() 
        return HttpResponse('پسورد شما تغییر یافت  ')



def get_mail(request):
    if request.method=='GET':
        return render(request,"accounts/get_mail.html")
    else:
        global user
        user = request.POST.get('username')
        u = User.objects.get(username=user)
        if request.POST.get('mail') == u.email:
            send_mail('code',random_code,settings.EMAIL_HOST_USER,[request.POST.get('mail')]) 

            return HttpResponseRedirect('faramooshi')
        else:
            context={'message':'نام کاربری و ایمیل با هم مطابقت ندارند'}
            
            return render(request,"accounts/get_mail.html",context)

def register(request):
    if request.method == 'POST':
        form=MyForm(request.POST)
        if form.is_valid():
            usermod=User.objects.create_user(username=request.POST['username'], password= request.POST['password'],email=request.POST['email'])
            usermod.save()
            return HttpResponse('ثبت نام شما در سایت صورت پذیرفت.')
    if request.method == 'GET':
        form=MyForm()
        return render(request,'accounts/register.html',{'form':form})
    
   
@login_required
def show_post(request):
    posts =Post.objects.all()

    return render(request,'accounts/show_post.html',{'posts':posts})
