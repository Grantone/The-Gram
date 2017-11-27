from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Profile

# Create your views here.


def index(request):
    # return render(request, 'all-posts/index.html')
    if not request.user.is_authenticated():
        redirect('login')

    # users_followed = request.user.profile.following.all()
    post = Post.objects.get(
        profile__in=users_followed).order_by('-posted_on')

    return render(request, 'all-posts/index.html', {
        'posts': posts
    })


@login_required(login_url='/accounts/login/')
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
    return render(request, 'all-posts/post.html', content)


@login_required
def profile(request):
    # user = User.objects.get(username=username)
    user = request.user
    if not user:
        return redirect('index')

    profile = Profile.objects.get(user=user)
    content = {
        'username': username,
        'user': user,
        'profile': profile
    }
    return render(request, 'all-posts/profile.html', context)


@login_required
def inbox(request):
    user = request.user

    return render(request, 'all-posts/inbox.html', content)


def login_user(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'registration/login.html', {
        'form': form
    })


def signout(request):
    logout(request)
    return redirect('index')


def followers(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    profiles = profile.followers.all

    context = {
        'header': 'Followers',
        'profiles': profiles,
    }

    return render(request, 'all-posts/follow_list.html', content)


def following(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    profiles = profile.following.all

    context = {
        'header': 'Following',
        'profiles': profiles
    }
    return render(request, 'all-posts/follow_list.html', content)
