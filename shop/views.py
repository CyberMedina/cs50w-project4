from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Sucursal, Categoria, Producto, Inventario
from django.views.decorators.csrf import csrf_exempt
import json

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



@csrf_exempt
def get_cart(request):
    if 'carrito' in request.session:
        print(request.session['carrito'])
        return JsonResponse(request.session['carrito'])
    else:
        return JsonResponse({})

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = Producto.objects.get(id=product_id)
        if 'carrito' not in request.session:
            request.session['carrito'] = {}
        request.session['carrito'][product_id] = {
            'cantidad': 1,
            'nombre': product.nombre,
            'precio': str(product.precio)
        }
        request.session.modified = True
        return JsonResponse({'status': 'ok'})

@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity'))
        if 'carrito' in request.session and product_id in request.session['carrito']:
            request.session['carrito'][product_id]['cantidad'] = quantity
            request.session.modified = True
        return JsonResponse({'status': 'ok'})

@csrf_exempt
def empty_cart(request):
    if request.method == 'POST':
        if 'carrito' in request.session:
            request.session['carrito'] = {}
            request.session.modified = True
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})






