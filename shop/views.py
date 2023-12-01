from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Sucursal, Categoria, Producto, Inventario
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def shop(request):
    sucursal_id = request.session.get('sucursal_id')
    query = request.GET.get('query')
    print(query)

    if sucursal_id is not None:
        inventario = Inventario.objects.filter(sucursal__id=sucursal_id, cantidad__gt=0)
        if query is not None:
            productos = Producto.objects.filter(
                Q(id__in=[item.producto.id for item in inventario]),
                Q(nombre__icontains=query) | Q(categoria__nombre__icontains=query)
            )
        else:
            productos = Producto.objects.filter(id__in=[item.producto.id for item in inventario])
    else:
        productos = Producto.objects.none()

    categorias = Categoria.objects.all()

    return render(request, 'shop/shop.html', context={'productos': productos, 'categorias': categorias, 'query': query})

@csrf_exempt
def set_sucursal(request, sucursal_id):
    if request.method == 'POST':
        try:
            sucursal = Sucursal.objects.get(pk=sucursal_id)
            request.session['sucursal_id'] = sucursal_id
            return JsonResponse({'status': 'success'})
        except Sucursal.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'La sucursal no existe'})





