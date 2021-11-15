from articles.models import Article
from django.shortcuts import render
from django.http import Http404


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def articles(request):
    return render(request, 'articles.html', {"posts": Article.objects.all()})