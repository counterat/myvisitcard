from django.http import HttpResponse
from .models import * 
from django.shortcuts import render

def index(request):
    all_posts = list(Post_blog.objects.all())[::-1]

    context = {
        'all_posts': all_posts,  # Передаем список всех постов в контекст шаблона
        'all_works': list(Works_blog.objects.all())[::-1]
    }
    return render(request, 'index.html', context=context)

def example(request, name=None):
    if name is None:
        return HttpResponse("undefined")
    else:
        return HttpResponse(name)
    return HttpResponse(f'{name}')

# Create your views here.
