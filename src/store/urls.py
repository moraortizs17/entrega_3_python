from django.urls import path
from . import views
from .views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', ProductoListView.as_view(), name='productos'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detalle'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('productos/<int:pk>/borrar/', ProductoDeleteView.as_view(), name='producto_borrar'),
    path('clientes/', views.clientes, name='clientes'),
    path('ordenes/', views.ordenes, name='ordenes'),
    path('categorias/', views.categorias, name='categorias'),
    path('about/', views.about, name='about'),
]