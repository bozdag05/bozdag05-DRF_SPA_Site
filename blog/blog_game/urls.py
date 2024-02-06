from django.urls import path
from .views import HomeView, PostView, register

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('<slug:slug>/', PostView.as_view(), name='post_detail'),
]
