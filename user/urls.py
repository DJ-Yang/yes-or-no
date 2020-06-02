from django.urls import path, include
from user import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('signin/', views.signin, name='signin'),
    path('add_info/', views.add_info, name='add_info'),
]
