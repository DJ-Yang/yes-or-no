from django.urls import path, include
from user import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('signin/', views.signin, name='signin'),
    path('add_info/', views.add_info, name='add_info'),
    path('get_form/', views.get_form, name='get_form'),
    path('user_info/', views.user_info, name='user_info'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

