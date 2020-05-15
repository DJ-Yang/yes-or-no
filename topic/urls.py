from django.contrib import admin
from django.urls import path, include
from . import views

app_name='topic'

urlpatterns = [
    path('topic/', views.topic_list, name="list"),
    path('topic/<int:topic_id>/', views.topic_select, name="select"),
    path('topic/<int:topic_id>/result/', views.topic_result, name="result"),
    path('topic/set/selection/', views.set_selection, name="set_selection"),
]