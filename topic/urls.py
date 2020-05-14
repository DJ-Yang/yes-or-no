from django.contrib import admin
from django.urls import path, include
from . import views

app_name='topic'

urlpatterns = [
    path('topic/', views.topic_list, name="topic_list"),
    path('topic/<int:topic_id>', views.topic_detail, name="topic_detail"),
]