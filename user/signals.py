from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from social_django.models import UserSocialAuth
from .models import CustomUser

@receiver(post_save, sender=UserSocialAuth)
def social_auth_registered(sender, instance, created, **kwargs):
    if created and instance.provider == 'google-oauth2':
        # Aquí puedes manejar los datos del usuario de Google como quieras
        # Por ejemplo, puedes guardar los datos en la sesión del usuario
        print("Llego aqui")

        # Actualiza solo el usuario que acaba de iniciar sesión
        instance.user.is_first_time_Google = True
        instance.user.save()