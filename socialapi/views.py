from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PostSerializer
from feeds.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
