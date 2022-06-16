from django.urls import path

from . import views

urlpatterns = [
    path('', views.subscribe, name='news_subscribe'),
    # path('unsub/<unsubscribe_key:unsubscribe_key>/', views.unsubscribe, name='news_unsubscribe'),

]
