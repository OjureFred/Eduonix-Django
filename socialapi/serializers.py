from rest_framework import serializers

from feeds.models import Post
from comments.models import Comment

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['heading', 'text', 'date', 'author']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'date', 'author', 'post']