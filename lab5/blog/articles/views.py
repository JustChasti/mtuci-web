from articles.models import Article
from django.shortcuts import render, redirect
from django.http import Http404


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
