from django.urls import path
from .views import HomeView, PostView, register, user_login, user_logout, ContactView, SuccessView, SearchView, TagView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchView.as_view(), name='search'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag'),
    path('<slug:slug>/', PostView.as_view(), name='post_detail'),
]
