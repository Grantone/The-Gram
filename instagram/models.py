from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User)
    post_image = models.ImageField(upload_to='posts/', null=True, blank=True)
    title = models.CharField(max_length=60)

    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post')
    comment = models.CharField(max_length=100)
