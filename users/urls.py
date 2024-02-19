from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logaut_view, name='logout'),
    path('profile/', show_profile,name='profile'),
    path('verify/',verify_code_view,name='verify')
]