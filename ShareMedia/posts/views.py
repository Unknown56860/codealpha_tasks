from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts':posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post':post})

@login_required(login_url='/users/login/')
def new_post(request):
    if request.method == 'POST':
        form = forms.create_post(request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect('posts:list')
    else:
        form = forms.create_post()
    return render(request, 'posts/new_post.html', {'form':form})
