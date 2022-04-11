from rest_framework import serializers

from feeds.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('heading', 'text', 'date', 'author')