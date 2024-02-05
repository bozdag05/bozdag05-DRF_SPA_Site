from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "blog_game/index.html"
    context_object_name = "posts"
    #paginate_by = 2