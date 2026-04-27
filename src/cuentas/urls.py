from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambiar_password/', auth_views.PasswordChangeView.as_view(template_name='cuentas/cambiar_password.html'), name='cambiar_password'),
    path('cambiar_password_hecho/', auth_views.PasswordChangeDoneView.as_view(template_name='cuentas/cambiar_password_hecho.html'), name='password_change_done'),
]
