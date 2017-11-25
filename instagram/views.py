from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # return render(request, 'all-posts/index.html')
    if not request.user.is_authenticated():
        redirect('login')

    users_followed = request.user.profile.following.all()
    posts = Post.objects.filter(
        user_profile__in=users_followed).order_by('-posted_on')

    return render(request, 'all-posts/index.html', {
        'posts': posts
    })


def post(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        like = Like.objects.get(post=post, user=request.user)
        liked = 1
    except:
        like = None
        liked = 0

    context = {
        'post': post,
        'liked': liked
    }
    return render(request, 'all-posts/post.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    if not user:
        return redirect('index')

    profile = Profile.objects.get(user=user)
    context = {
        'username': username,
        'user': user,
        'profile': profile
    }
    return render(request, 'all-posts/profile.html', context)
