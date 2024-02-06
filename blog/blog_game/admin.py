from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "author", "image", "url", "is_published")
    list_editable = ("is_published",)
    prepopulated_fields = {'url': ['title']}


admin.site.register(Post, PostAdmin)
