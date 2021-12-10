from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request):
    template_group_posts = 'posts/group_list.html'
    return render(request, template_group_posts)

def show_base(request):
    template_base = 'templates/base.html'
    return render(request, template_base)