from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register_user/", views.register_user, name="register_user"),
    path("register_userG/", views.register_userG, name="register_userG"),
    path("register_user_API/", views.register_user_API, name="register_user_API"),
    path("register_user_location/", views.register_user_location, name="register_user_location"),
    path("validation_register_API/", views.validation_register_API, name="validation_register_API"),
    path("register_location_API/", views.register_location_API, name="register_location_API"),
        path("locations_user/", views.locations_user, name="locations_user"),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]