from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import UserRegisterForm, UserLoginForm, ContactForm, CommentForm
from taggit.models import Tag


class HomeView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=False)
    template_name = "blog_game/index.html"
    context_object_name = "posts"
    ordering = "-created_at"
    paginate_by = 6


class PostView(DetailView):
    model = Post
    template_name = "blog_game/post_detail.html"
    context_object_name = "post"
    slug_field = "url"
    comment_form = CommentForm()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["lasts_posts"] = Post.objects.all().order_by('-id')[:3]
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, slug,  *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, "blog_game/post_detail.html", context={'comment_form': comment_form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации")

    else:
        form = UserRegisterForm()

    return render(request, "blog_game/register.html", context={"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, 'Вы успешно авторизовались')
                login(request, user)
                return redirect("home")
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()

    return render(request, "blog_game/login.html", context={"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, "blog_game/contact.html", context={"form": form, "title": "Тех. поддержка"})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(f" От {name} | {subject}", message, email, ["muhammadosmanov02@gmail.com"])
            except BadHeaderError:
                messages.error(request, "Невалидный загаловок")
            messages.success(request, "Ваше письмо отправлено")
        return render(request, "blog_game/success.html", context={"form": form})


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog_game/success.html', context={"title": "جزاكم الله خيرا"})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        results = ''
        if query:
            results = Post.objects.filter(title__icontains=query)
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "blog_game/search.html", context={
            'title': 'search',
            'results': page_obj,
            'count': paginator.count,
        })


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tag=tag)
        common_tag = Post.tag.most_common()
        return render(request, "blog_game/tag.html", context={
            "title": f'#ТЕГ {tag}'.upper(),
            "posts": posts,
            "common_tag": common_tag,
        })