from django.shortcuts import render, get_object_or_404
from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


context = {
    "title": "Это главная страница проекта Yatube",
    "posts_title": "Здесь будет информация о группах проекта Yatube",
          }