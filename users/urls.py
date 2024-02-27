from django.urls import path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logaut_view, name='logout'),
    path('profile/', show_profile, name='profile'),
    path('verify/', verify_code_view, name='verify'),
    path('update/', update_view, name='update'),
    path('follow/<int:pk>/', following_view, name='follow'),
    path('username/<int:pk>/', get_user_by_username, name='username'),
]


