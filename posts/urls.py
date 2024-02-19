from django.urls import path
from posts.views import *
app_name = 'posts'

urlpatterns = [
    path('add/post/', add_post_view, name='add'),
    path('post/<int:pk>', post_detail_view,name='detail'),
    path('', home_pages_view, name='home'),
    path('post/comment/<int:pk>/', comment_view, name='comment')
]
