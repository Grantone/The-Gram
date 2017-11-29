from django import forms
from .models import Profile, Post
from django.contrib.auth.models import User


class InstagramLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'description', 'following', 'followers')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
