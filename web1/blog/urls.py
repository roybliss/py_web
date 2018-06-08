from django.contrib import admin
from django.urls import path, include, re_path
from . import views


app_name = 'blog'
urlpatterns = [
   re_path(r'^$', views.index),
   re_path(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
   re_path(r'^add/(?P<article_id>\d+)$', views.add_page, name='add_page'),
   re_path(r'^add_action/$', views.add_action, name='add_action'),
]