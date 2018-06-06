from django.contrib import admin
from django.urls import path, include, re_path
from cmdb import views

urlpatterns = [
   re_path(r'^$', views.index),
]