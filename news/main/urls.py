from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<slug:cat>', views.categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
]


