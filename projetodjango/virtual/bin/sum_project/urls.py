from django.contrib import admin
from django.urls import path

from sum_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_page, name='register_page'),  # Alterei a rota de 'register.html' para 'register/'
    path('ClienteForm/', views.ClienteForm, name='ClienteForm'),
]
