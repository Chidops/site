from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    path('login/', views.login, name='login'),
    path('addpage/', views.addpage, name='add_page'),
    path('cats/<slug:cat>', views.categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
]


