from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Post


def home(request):
     
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context)

def about(request):
     return render(request, 'blog/about.html', {'title': 'About'})