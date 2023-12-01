from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('set_sucursal/<int:sucursal_id>/', views.set_sucursal, name='set_sucursal'),

]