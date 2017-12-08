from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.dispatch import receiver
from tinymce.models import HTMLField
from vote.models import VoteModel
from vote.managers import VotableManager


# UP = 0
# DOWN = 1
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey('Post')
    comment = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(
        'Profile', related_name="followers_profile", blank=True)
    following = models.ManyToManyField(
        'Profile', related_name="following_profile", blank=True)
    profile_pic = ProcessedImageField(upload_to='profile_pics', format='JPEG', options={
                                      'quality': 100}, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.user.username


class Like(models.Model):
    post = models.ForeignKey('Post')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title


class Post(models.Model):
    user = models.ForeignKey(User)
    post_image = models.ImageField(upload_to='posts/', null=True, blank=True)
    title = models.CharField(max_length=60)
    upvote_count = models.PositiveIntegerField(default=0)
    downvote_count = models.PositiveIntegerField(default=0)

    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all()
        return posts

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    @classmethod
    def get_single_post(cls, pk):
        post = cls.objects.get(pk=pk)

        return post


class Review(models.Model):
    users = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vote")
    photos = models.ForeignKey(Post, related_name="vote")
    comment = models.CharField(max_length=140, blank=True)

    def save_review(self):
        self.save()
