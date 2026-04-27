from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import UserForm, PerfilForm

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user)
            return redirect('login')
    else:
        form = RegistroForm()
    
    return render(request, 'cuentas/registro.html', {'form': form})

@login_required
def perfil(request): 
    perfil = request.user.perfil
    return render(request, 'cuentas/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('perfil')
    else:
        user_form = UserForm(instance=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)
    
    return render(request, 'cuentas/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })