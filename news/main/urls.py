from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', views.PostCategory.as_view(), name='category'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('cats/<slug:cat>', views.categories),
    path('contact/', views.contact, name='contact'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
]


