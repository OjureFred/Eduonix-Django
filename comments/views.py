from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comment

class CreateNewComment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'feeds/detail.html'
    fields = ['text']
    success_url = '/'
