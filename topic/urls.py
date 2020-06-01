from django.contrib import admin
from django.urls import path, include
from . import views

app_name='topic'

urlpatterns = [
    path('', views.topic_list, name="list"),
    path('<int:topic_id>/', views.topic_select, name="select"),
    path('<int:topic_id>/result/', views.topic_result, name="result"),
    path('set/selection/', views.set_selection, name="set_selection"),
    path('request/', views.user_request, name="request"),
]