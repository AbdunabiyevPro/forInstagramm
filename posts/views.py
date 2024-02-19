from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import PostModelForm
from posts.models import PostModel, CommentModel


def home_pages_view(request):
    posts = PostModel.objects.all()
    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)
    context = {
        'posts': posts
    }
    return render(request, 'index.html',context=context)


@login_required
def add_post_view(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            PostModel.objects.filter(user=request.user).all()
            return redirect('posts:home')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'add-post.html', context)


def post_show(request):
    pass



@login_required
def comment_view(request, pk):
    post = PostModel.objects.get(pk=pk)
    if post:
        if request.method == 'POST':
            user = request.user
            comment = request.POST.get('comment')

            new_comment = CommentModel.objects.create(post=post,user=user,comment=comment)
            new_comment.save()
            return redirect(request.GET.get('next'))
    else:
        text = 'Post does not found'
        return HttpResponse(text)

def post_detail_view(request,pk):
    post = PostModel.objects.get(pk=pk)

    if post:
        comments = post.comment.all()
        context = {
            'post': post,
            'comments': comments
        }
        return render(request,'post-detail.html',context)
    else:
        text = 'Post does not found'
        return HttpResponse(text)


