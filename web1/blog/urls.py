from django.contrib import admin
from django.urls import path, include, re_path
from . import views


app_name = 'blog'
urlpatterns = [
   re_path(r'^$', views.index),
   re_path(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
]