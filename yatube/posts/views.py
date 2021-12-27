from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 
    

def group_posts(request, pk):
    return render(request, 'posts/group_list.html', context)

context = {
    "title" : "Это главная страница проекта Yatube",
    "posts_title" : "Здесь будет информация о группах проекта Yatube",
    }