from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.order_by('created')[:10]
    return render_to_response('index.html', {'posts': posts})


def category(request, id):
    posts = Post.objects.filter(category=id).order_by('created')[:10]
    return render_to_response('category.html', {'posts': posts})


def categories(request):
    posts = Post.objects.order_by('created')[:10]
    return render_to_response('category.html', {'posts': posts})
