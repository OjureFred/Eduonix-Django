from django.db import models

class Post(models.Model):
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading[0:30]