from django.shortcuts import render
from .models import Sucursal, Categoria, Producto, Inventario

# Create your views here.

def shop(request):

    # Se obtienen todos los productos

    productos = Producto.objects.all()

    categorias = Categoria.objects.all()






    return render(request, 'shop/shop.html', context={'productos': productos, 'categorias': categorias})


