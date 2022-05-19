from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'