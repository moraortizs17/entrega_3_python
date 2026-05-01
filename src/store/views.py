from django.shortcuts import render
from .models import Cliente, Producto, Ordenes, Categorias
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'store/index.html')

class ProductoListView(ListView):
    model = Producto
    template_name = 'store/productos.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'store/producto_detalle.html'
    context_object_name = 'producto'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'store/producto_form.html'
    fields = ['nombre', 'marca', 'precio', 'stock', 'categoria', 'descripcion', 'foto_producto']
    success_url = reverse_lazy('productos')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'store/producto_form.html'
    fields = ['nombre', 'marca', 'precio', 'stock', 'categoria', 'descripcion', 'foto_producto']
    success_url = reverse_lazy('productos')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'store/producto_confirmar_borrar.html'
    success_url = reverse_lazy('productos')

@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'store/clientes.html', {'clientes': clientes})

@login_required
def ordenes(request):
    ordenes = Ordenes.objects.all()
    return render(request, 'store/ordenes.html', {'ordenes': ordenes})

def categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'store/categorias.html', {'categorias': categorias})

def about(request):
    return render(request, 'store/about.html')