from django.urls import path

from . import views

urlpatterns = [
    path('', views.subscribe, name='news_subscribe'),
    path('/<slug:slug>/', views.unsubscribe, name='news_unsubscribe'),

]
