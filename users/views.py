import random

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from conf.settings import EMAIL_HOST_USER
from users.forms import RegistrationForm, LoginForm


def send_activation_email(email):
    subject = "Activation code"
    code = str(random.randint(1000, 9999))
    sender = EMAIL_HOST_USER
    recipient_list = [email]
    if send_mail(subject, code, sender, recipient_list):
        return True
    return False

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.is_active = True
            #send_activation_email(form.cleaned_data['email'])

            form.save()
            return redirect('users:login')
    else:
        return render(request, 'register.html')




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('post:home')
    else:
        return render(request, 'login.html')



def logaut_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('posts:home')