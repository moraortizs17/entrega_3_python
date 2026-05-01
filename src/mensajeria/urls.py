from django.urls import path
from . import views

urlpatterns = [
    path('recibidos/', views.recibidos, name='recibidos'),
    path('enviados/', views.enviados, name='enviados'),
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
]
