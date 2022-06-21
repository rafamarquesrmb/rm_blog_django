from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('tags/', views.all_tags, name='all_tags'),
    path('categories/', views.all_categories, name='all_categories'),
    path('tag/<slug:slug>/', views.tags, name='tag_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
]
