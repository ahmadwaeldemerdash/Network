from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    text = models.CharField(max_length=600)
    time = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    def serialize(self):
       return {
            'user': self.user.username,
            'text' : self.text,
            'time' : self.time,
            'likes': self.likes,
        }

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")
