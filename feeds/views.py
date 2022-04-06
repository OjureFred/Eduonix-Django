from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from followers.models import Follower

class HomePage(TemplateView):
    http_method_names = ['get']
    template_name = 'feeds/homepage.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, *args,  **kwargs):
        context =  super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            following = list(Follower.objects.filter(followed_by = self.request.user).values_list('following', flat=True))
            posts = Post.objects.filter(user_in = following).order_by('-id')[0:30]
        else:
            posts = Post.objects.all().order_by('-id')[0:30]
        
        context['posts'] = posts
        return context
    
class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = 'feeds/detail.html'
    model = Post
    context_object_name = 'post'

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'feeds/create.html'
    fields = ['heading', 'text']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    
