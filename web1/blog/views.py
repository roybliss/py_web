from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def add_page(request, article_id):
    if str(article_id) == 0:
        return render(request, 'blog/add_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/add_page.html', {'article': article})

def add_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    return HttpResponseRedirect('/blog/')