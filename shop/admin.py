from django.contrib import admin
from .models import Sucursal, Categoria, Producto, Inventario

# Register your models here.

admin.site.register(Sucursal)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Inventario)
