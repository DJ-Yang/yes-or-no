from django.urls import path, include
from user import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('signin/', views.signin, name='signin'),
]
