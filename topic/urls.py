from django.contrib import admin
from django.urls import path, include
from . import views

app_name='topic'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('topic/', views.topic_list, name="topic_list")
]