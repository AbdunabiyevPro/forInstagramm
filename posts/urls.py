from django.urls import path
from posts.views import home_pages_view

app_name = 'posts'

urlpatterns = [
    path('', home_pages_view, name='home')
]
