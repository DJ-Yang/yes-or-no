from django.contrib import admin
from django.urls import path, include
from . import views

app_name='topic'

urlpatterns = [
    path('', views.topic_list, name="list"),
    path('<int:topic_id>/check/', views.check_selection, name="check_selection"),
    path('<int:topic_id>/', views.topic_select, name="select"),
    path('<int:topic_id>/result/', views.topic_result, name="result"),
    path('request/', views.user_request, name="request"),
]