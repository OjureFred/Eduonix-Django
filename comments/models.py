from django.db import models
from django.contrib.auth.models import User

from feeds.models import Post

class Comment(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text
