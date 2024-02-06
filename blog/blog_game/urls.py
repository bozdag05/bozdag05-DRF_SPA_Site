from django.urls import path
from .views import HomeView, PostView, register, user_login, user_logout

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('<slug:slug>/', PostView.as_view(), name='post_detail'),
]
