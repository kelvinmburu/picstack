from django.urls import path
from post.views import index, NewPost


urlpatterns = [
    path('', index, name='index'),
    path('newpost/', NewPost, name='newpost'),
]
