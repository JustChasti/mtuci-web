from django.http.response import HttpResponseForbidden, HttpResponseNotAllowed
from articles.models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login




def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def articles(request):
    return render(request, 'articles.html', {"posts": Article.objects.all()})


def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                try:
                    post = Article.objects.get(title=form["title"])
                    form['errors'] = u"Пост с таким именем уже существует"
                    return render(request, 'create_post.html', {'form': form})
                except Exception as e:
                    id = Article.objects.create(text=form["text"], title=form["title"], author=request.user).id
                    return redirect('get_article', article_id=id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})

    else:
        raise Http404


def registration(request):
    if request.method == "POST":
        form = {
                'username': request.POST["username"], 'password': request.POST["password"], 'email': request.POST["email"]
            }
        if form["username"] and form["password"] and form["email"]:
            try:
                User.objects.get(username=form["username"])
                raise HttpResponseForbidden
            except Exception as e:
                User.objects.create_user(form["username"], form["email"], form["password"])
                return redirect('loggin')
        else:
            raise HttpResponseNotAllowed
    else:
        return render(request, 'registration.html', {})


def loggin(request):
    if request.method == "POST":
        form = {
                'username': request.POST["username"], 'password': request.POST["password"]
            }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user:
                login(request, user)
                return redirect('articles')
        else:
            raise HttpResponseNotAllowed
    else:
        return render(request, 'login.html', {})
