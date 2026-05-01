from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateTimeField(null= True, blank=True)
    telefono = PhoneNumberField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.apellido.upper()} - {self.nombre.upper()}"
    
class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado_categoria = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        estado = "Activo" if self.estado_categoria else "Inactivo"
        return f"{self.nombre_categoria} - {estado}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True)
    marca = models.CharField(max_length=100)
    descripcion = RichTextField()
    foto_producto = models.ImageField(upload_to='foto_productos/',null=True, blank=True)
    fecha_inventario = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} | $ {self.precio}"

class Ordenes(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_de_orden = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Ordenes"

    def __str__(self):
        return f"Orden de {self.cliente} - {self.producto}"

