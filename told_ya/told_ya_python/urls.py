from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('voting/', views.voting, name='voting'),
    path('phone-input/', views.phone_input, name='phone_input'),
    path('user/', views.user, name='user'),
    path('argument/', views.argument, name='argument'),
]