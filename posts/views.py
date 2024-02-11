from django.shortcuts import render
from posts.models import PostModel


def home_pages_view(request):
    posts = PostModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html',context=context)