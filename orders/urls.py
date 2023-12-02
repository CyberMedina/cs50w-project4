from django.urls import path, include
from . import views

urlpatterns = [
    path('pruebitaWhatsapp/', views.pruebitaWhatsapp, name='pruebitaWhatsapp'),
]