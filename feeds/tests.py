from django.urls import reverse
from django.test import TestCase

from django.contrib.auth.models import User

from .models import Post
from profiles.models import Profile

class PostCreateViewTest(TestCase):
    def post_test_create_user(self):
        user1 = User.objects.create(
            username = "user1", email = "user1@gmail.com", password = "12345"
        )

        feed_test = {
            'heading': "Feed heading", 
            'text' : "Feed text" 
        }

        self.client.force_login(user1)
        self.client.post(reverse('feeds:new_post'), feed_test)

        self.assertTrue(Post.objects.filter(author= user1).exists)