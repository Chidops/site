from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.models import *

from main.forms import AddPostForm
from main.utils import DataMixin

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
#        {'title': 'Войти', 'url_name': 'login'}
        ]


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm(request.POST)
    return render(request, 'main/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def skip(request):
    return redirect('blog/')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))


def contact(request):
    return HttpResponse('')


def login(request):
    return HttpResponse('')


def show_post(request, post_slug):
    post = get_object_or_404(Post, pk=post_slug)
    context = {
        'posts': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'main/post.html', context=context)


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


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
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
