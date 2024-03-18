from django.contrib import admin
from django.urls import path

from sum_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_page, name='register_page'),
    path('register_item/', views.register_item, name='register_item'),
    path('ClienteForm/', views.ClienteForm, name='ClienteForm'),
    path('PedidoForm/', views.PedidoForm, name='PedidoForm'),
]
