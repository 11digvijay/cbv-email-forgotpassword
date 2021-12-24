from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
# Create your views here.
def loginview(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(username=un,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('show_lap')
        else:
            messages.error(request,'Invalid credentials')
    tempname_name = 'authapp/login.html'
    return render(request,tempname_name)

otp = None
user = None
def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            global user
            username = request.POST['username']
            email = request.POST['email']
            form.save()
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            global otp
            otp = random.randint(1000, 9999)
            subject = 'verification otp'
            message = f'Hi {username}, thank you for registering.Your email verification OTP is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect("otp_verify")
    context = {'form':form}
    template_name = 'authapp/register.html'
    return render(request,template_name, context)

def logoutview(request):
    logout(request)
    return redirect('login')


def otpVerifyView(request):
    if request.method == 'POST':
        num = request.POST.get('otp')
        if int(num) == otp:
            user.is_active = True
            user.save()
            return redirect("login")
        else:
            messages.error(request,"Invalid otp")
    template_name = 'authapp/otpverify.html'
    context = {}
    return render(request, template_name, context)