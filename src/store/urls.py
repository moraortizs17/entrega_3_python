from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('ordenes/', views.ordenes, name='ordenes'),
    path('categorias/', views.categorias, name='categorias'),
]