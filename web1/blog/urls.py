from django.contrib import admin
from django.urls import path, include, re_path
from . import views


app_name = 'blog'
urlpatterns = [
   re_path(r'^$', views.index),
   re_path(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
   re_path(r'^edit/(?P<article_id>\d+)$', views.edit_page, name='edit_page'),
   re_path(r'^edit_action/$', views.edit_action, name='edit_action'),
]