from django.urls import path, include
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('pruebitaWhatsapp/', views.pruebitaWhatsapp, name='pruebitaWhatsapp'),
]