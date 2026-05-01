from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_filter = ("remitente", "fecha",)
    list_display = ("remitente", "destinatario", "fecha",)
    search_fields = ("remitente",)


