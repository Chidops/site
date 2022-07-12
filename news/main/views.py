from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from main.models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'main/index.html', context=context)


def index(request, cat_id):
    posts = Post.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О нас'})


def categories(request, cat):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям<h1><p>{cat}")


def archive(request, year):
    if int(year) > 2022:
        return redirect('/home', permanent=True)
    return HttpResponse(f"<h1> Архив по годам</h1><P>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
