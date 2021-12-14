from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    return render(request, template, context)

def group_posts(request):
    template_group_posts = 'posts/group_list.html'
    return render(request, template_group_posts, context)

context = {
    "title" : "Это главная страница проекта Yatube",
    "posts_title" : "Здесь будет информация о группах проекта Yatube",
    }