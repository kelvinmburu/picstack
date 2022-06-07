from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('main/', views.main, name='main'),
    path('post/', views.post, name='post'),
    path('tag/', views.tag, name='tag'),
    path('profile/', views.profile, name='profile')
]