from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading[0:30]