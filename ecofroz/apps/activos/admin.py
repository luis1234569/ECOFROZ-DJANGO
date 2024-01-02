from django.contrib import admin

# Register your models here.

from .models import desc_activo, Imagenes

class ImageInline(admin.TabularInline):
    model = Imagenes


@admin.register(desc_activo)
class ActivoAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]