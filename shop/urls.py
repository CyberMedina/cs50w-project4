from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('set_sucursal/<int:sucursal_id>/', views.set_sucursal, name='set_sucursal'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('get_cart/', views.get_cart, name='get_cart'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),

]