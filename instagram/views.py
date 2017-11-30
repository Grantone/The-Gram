from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Profile
from .forms import UserProfileForm, NewPostForm

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'all-posts/index.html', {
        'posts': posts
    })


@login_required(login_url='/accounts/login/')
def post(request, pk):
    post = Post.objects.get(pk=post_id)
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


# @login_required
# def profile(request):
#     # user = User.objects.get(username=username)
#     user = request.user
#     if not user:
#         return redirect('index')
#
#     profile = Profile.objects.get(user=user)
#     content = {
#         'username': username,
#         'user': user,
#         'profile': profile
#     }
#     return render(request, 'all-posts/profile.html', context)


@login_required(login_url='/accounts/login/')
def inbox(request):
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


@login_required
def profile(request):
    post = Post.objects.all()
    return render(request, 'all-posts/profile.html', {"post": post})


@login_required(login_url='/accounts/login/')
def update_user_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        user_profile = UserProfileForm(
            request.POST, instance=request.user.profile)

        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(index)
        # else:
        #     messages.error(
        #         follower request, 'A slight error please correct,,, can you try again')

    else:
        user_form = UserProfileForm(instance=request.user)
        user_profile = UserProfileForm(instance=request.user.profile)

    return render(request, 'all-posts/edit_profile.html', {'user_form': user_form, 'user_profile': user_profile, })


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if current_user.is_authenticated and form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(index)
    else:
        form = NewPostForm()
    return render(request, 'posts/new-post.html', {"form": form})


@login_required
def add_like(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
