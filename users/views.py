import random
from datetime import datetime, timedelta

import pytz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from conf.settings import EMAIL_HOST_USER
from posts.models import PostModel
from users.forms import RegistrationForm, LoginForm
from users.models import VerificationCodeModel, UserModel


def send_activation_email(email):
    subject = "Activation code"
    code = str(random.randint(1000, 9999))
    sender = EMAIL_HOST_USER
    recipient_list = [email]
    if send_mail(subject, code, sender, recipient_list):
        new_code = VerificationCodeModel.objects.create(code=code,email=email)
        new_code.save()
        return True
    return False

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.is_active = True
            send_activation_email(form.cleaned_data['email'])

            form.save()
            return render(request,'verify-code.html')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'register.html')




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:home')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'login.html')



def logaut_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('posts:home')


@login_required
def show_profile(request):
    if request.method == 'GET':
        users_posts = PostModel.objects.filter(user=request.user).all()
        context = {
            'users_posts': users_posts
        }
        return render(request, 'show-profile.html', context=context)

def verify_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        code = VerificationCodeModel.objects.filter(code=code).first()
        tashkent_timezone = pytz.timezone('Asia/Tashkent')
        current_datatime_tashkent = datetime.now(tashkent_timezone)
        if current_datatime_tashkent - timedelta(minutes=2) <= code.send_time:
            UserModel.objects.update(is_active=True)
            VerificationCodeModel.objects.filter(code=code).delete()
            return redirect('users:login')
        else:
            text = "Your code is invalid"
            return HttpResponse(text)




