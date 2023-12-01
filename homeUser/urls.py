from django.urls import path
from . import views



urlpatterns = [
    path('', views.homeUser, name='homeUser')
]