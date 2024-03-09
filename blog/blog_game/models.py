from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tag = TaggableManager()
    url = models.SlugField(allow_unicode=True, verbose_name='ссылка')
    information_card = RichTextUploadingField(blank=True, verbose_name='краткая информация')
    description = RichTextUploadingField(blank=True, verbose_name='Описание')
    image = models.ImageField(blank=True, verbose_name='картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обнавлено')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор поста')
    is_published = models.BooleanField(default=0, verbose_name='Черновик')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"