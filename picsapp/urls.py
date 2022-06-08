from django.urls import path
from picsapp.views import Signup, EditProfile
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', authViews.LoginView.as_view(template_name='picsapp/login.html'), name='login'),
    path('signup/', Signup, name='signup'),
    path('profile/edit', EditProfile, name='edit-profile')
]