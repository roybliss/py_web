from django.contrib import admin
from django.urls import path, include
from cmdb import views

urlpatterns = [
   path('', views.index),
]