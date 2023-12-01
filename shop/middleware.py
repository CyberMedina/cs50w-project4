from .models import Sucursal

class LoadSucursalesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        sucursales = Sucursal.objects.all()
        request.sucursales = sucursales
        sucursal_id = request.session.get('sucursal_id')
        if sucursal_id is not None:
            try:
                sucursal = Sucursal.objects.get(pk=sucursal_id)
                request.sucursal_seleccionada = sucursal.nombre
            except Sucursal.DoesNotExist:
                request.sucursal_seleccionada = None
        else:
            if sucursales:
                request.session['sucursal_id'] = sucursales[0].id
                request.sucursal_seleccionada = sucursales[0].nombre
            else:
                request.sucursal_seleccionada = None
        response = self.get_response(request)
        return response