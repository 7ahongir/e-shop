from django.shortcuts import render, get_object_or_404
from .models import *

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'main/blog.html', context)

