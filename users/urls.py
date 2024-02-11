from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view,name='login'),
    path('login/', logaut_view, name='logout')
]