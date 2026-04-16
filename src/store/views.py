from django.shortcuts import render
from .models import Cliente, Producto, Ordenes, Categorias

def index(request):
    return render(request, 'store/index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'store/productos.html', {'productos': productos})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'store/clientes.html', {'clientes': clientes})

def ordenes(request):
    ordenes = Ordenes.objects.all()
    return render(request, 'store/ordenes.html', {'ordenes': ordenes})

def categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'store/categorias.html', {'categorias': categorias})