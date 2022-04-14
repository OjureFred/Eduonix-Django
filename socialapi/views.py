from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PostSerializer, CommentSerializer

from feeds.models import Post
from comments.models import Comment

class PostViewSet(viewsets.ModelViewSet):
    '''
    API endpoint to allow Posts to be viewed and edited
    '''
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentsViewSet(viewsets.ModelViewSet):
    '''
    API endpoint to allow Comments to be viewed and edited
    '''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

