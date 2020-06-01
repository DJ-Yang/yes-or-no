from django.contrib import admin
from django.urls import path, include
from . import views

app_name='notice'

urlpatterns = [
  path('', views.notice, name="notice"),
  path('detail/<int:id>', views.notice_detail, name="notice_detail"),
]