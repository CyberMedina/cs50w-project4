from django.urls import path
from . import views


urlpatterns = [
    path("register_user/", views.register_user, name="register_user"),
    path("register_user_API/", views.register_user_API, name="register_user_API")
]