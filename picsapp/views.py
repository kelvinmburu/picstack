from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'picsapp/index.html',context)

def login(request):
    context = {}
    return render(request, 'picsapp/login.html')

def register(request):
    context = {}
    return render(request, 'picsapp/register.html')

def main(request):
    context = {}
    return render(request, 'picsapp/main.html')

def post(request):
    context = {}
    return render(request, 'picsapp/post_detail.html')

def tag(request):
    context = {}
    return render(request, 'picsapp/tag.html')

def profile(request):
    context = {}
    return render(request, 'picsapp/profile.html')
