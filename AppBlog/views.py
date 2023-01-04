from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from AppBlog.forms import *

def posts(request):
    return render(request, "AppBlog/posts.html")



def inicio(request):
    return render(request, "AppBlog/inicio.html")

