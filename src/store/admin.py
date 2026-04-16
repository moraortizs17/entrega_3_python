from django.contrib import admin
from store import models

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido"
    "", "email")
    search_fields = ("apellido", "nombre", "email")
    ordering = ("apellido", "nombre")

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_filter = ("nombre",)
    list_display = ("nombre", "precio", "stock")
    search_fields = ("nombre",)

@admin.register(models.Ordenes)
class OrdenesAdmin(admin.ModelAdmin):
    list_display = ("producto", "cliente", "cantidad")

@admin.register(models.Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_filter = ("nombre_categoria",)
    list_display = ("nombre_categoria", "estado_categoria")
