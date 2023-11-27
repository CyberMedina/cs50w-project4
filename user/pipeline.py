from django.shortcuts import redirect

def redirect_to_register_if_first_time(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2' and user.is_first_time_Google:
        user.is_first_time_Google = False
        user.save()
        return redirect('register_user')