from django.contrib.auth.models import User
from django.forms import SlugField
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from feeds.models import Post

class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author = user).count()

        return context

class FollowView(LoginRequiredMixin, View):
    pass