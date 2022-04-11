from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from followers.models import Follower
from comments.models import Comment
from comments.forms import CommentForm

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
            if not following:
                posts = Post.objects.all().order_by('-id')[0:30]
            else:
                posts = Post.objects.filter(author__in = following).order_by('-id')[0:30]
           
        else:
            posts = Post.objects.all().order_by('-id')[0:30]
        
        context['posts'] = posts
        return context
    
class PostDetailView(TemplateView):
    http_method_names = ['get']
    template_name = 'feeds/detail.html'
    model = Post
    success_url = 'feeds/detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        

        form = CommentForm()
        post = Post.objects.get(pk=pk)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context
    
    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.post = self.request.post
        obj.save()
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        comment = Comment.objects.create(
            text = request.POST.get.text,
            author = request.user,
            post = request.POST.get.post,
        )
        print(request.POST)

        return render(request, '/', 
        {
            'post': post,
            'comments': comments,
            'form': form
        }
         )

    
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
    
    def post(self, request, *args, **kwargs):

        post = Post.objects.create(
            text=request.POST.get("text"),
            author=request.user,
        )

        return render(
            request,
            "includes/post.html",
            {
                "post": post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )
    
