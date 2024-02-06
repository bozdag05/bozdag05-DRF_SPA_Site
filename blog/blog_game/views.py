from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import UserRegisterForm


class HomeView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=False)
    template_name = "blog_game/index.html"
    context_object_name = "posts"
    ordering = "-created_at"
    paginate_by = 2


class PostView(DetailView):
    model = Post
    template_name = "blog_game/post_detail.html"
    context_object_name = "post"
    slug_field = "url"


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect("/")

    else:
        form = UserRegisterForm()

    return render(request, "blog_game/register.html", context={"form": form})
