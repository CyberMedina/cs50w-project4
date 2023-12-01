from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
import user
from .models import StaffLocation, NoStaffLocation, CustomUser
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from social_django.models import UserSocialAuth


from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.



# Vista para redirigir cuando el usuario se autentica por Google
def register_userG(request):

    # Si el usuario está autenticado y es la primera vez que se autentica por Google
    if request.user.is_authenticated and request.user.is_first_time_Google:

        # Se cambia el estado de is_first_time_Google a False
        request.user.is_first_time_Google = False
        request.user.save()


        return render(request, 'users/register_userG.html')
    
    # Si el usuario no es su primera vez que se autentica por Google simplemente entra a la página principal
    else:
        return redirect('/')
    

@login_required
def register_user_location(request):
     return render(request, 'users/register_userG.html')
    




def register_user(request):
    return render(request, 'users/register_user.html')

def validation_register_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)

        if CustomUser.objects.filter(email=data['email']).exists():
            return JsonResponse({'status': 'error', 'message': 'El correo electrónico ya está registrado!'})
        

        CustomUser.objects.create_user(
            
            username = data['email'],
            email= data['email'],
            password= data['password'],
            first_name= data['name'],
            last_name=data['lastname']
        )

        user = authenticate(username=data['email'], password=data['password'])
        print(user)
        if user is not None:
            auth_login(request, user)

            return JsonResponse({'status': 'success', 'message' : 'Ha iniciado sesión!'})


        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})



def register_user_API(request):
    if request.method == 'POST':
        # data = json.loads(request.body)

        # print(data)

      

        # if User.objects.filter(email=data['email']).exists():
        #     return JsonResponse({'status': 'error', 'message': 'El correo electrónico ya está registrado!'})

        # if NoStaffLocation.objects.filter(telephone_Number=data['telephoneNumber']).exists():
        #     return JsonResponse({'status': 'error', 'message': 'El número de teléfono ya ha sido registrado!'})

        # # Procesa los datos según tus modelos
        # person_instance = Person.objects.create(
        #     name=data['name'],
        #     lastname=data['lastname']
        # )

        # location_instance = Location.objects.create(
        #     person=person_instance,
        #     adress_input=data['addressInput'],
        #     latitude=data['latitude'],
        #     longitude=data['longitude'],
        #     house_Number=data['houseNumber'],
        #     delivery_Instructions=data['text'],
        #     telephone_Number=data['telephoneNumber'],
        #     direction_Name=data['radio2']
        # )

        # user_instance = User.objects.create(
        #     Person=person_instance,
        #     email=data['email'],
        #     password=make_password(data['password'])
        # )



        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

def login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user_social_auth = UserSocialAuth.objects.filter(uid=email).first()


        if user_social_auth is None:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth_login(request, user)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Usuario o contraseña incorrectos'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Usted ha sido registrado por Google, por favor autentiquese con Google'})

        


    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') + '?openModal=true')


def register_by_access_token(request, backend):
    # backend es el nombre del proveedor de autenticación social, en este caso 'google'
    token = request.POST.get('access_token')
    try:
        # registra al usuario
        user = backend.do_auth(token)
    except Exception as e:
        return JsonResponse({"error": str(e)})

    if user and user.is_active:
        # si el usuario ya existe, no inicies sesión
        logout(request)
        return JsonResponse({"status": 'Usuario ya registrado.'}, status=400)

    # si es un nuevo usuario, guarda los datos pero no inicies sesión
    UserSocialAuth.objects.create(user=user, provider=backend.name, uid=user.email)
    logout(request)
    return JsonResponse({"status": 'Usuario registrado exitosamente.'})

@csrf_exempt
def register_location_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        user = request.user
        if user.is_authenticated:
            try:
                direction_name = data.get('selectedRadioButton')
                if not direction_name:
                    return JsonResponse({'status': 'error', 'message': 'Por favor rellena los campos necesarios!'}, status=400)
                location = NoStaffLocation(
                    user=user,
                    adress_input=data['addressInput'],
                    direction_Name=direction_name,
                    house_Number=data['houseNumber'],
                    telephone_Number=data['telephoneNumber'],
                    latitude=data['latitude'],
                    longitude=data['longitude'],
                    delivery_Instructions=data['text']
                )
                location.save()
                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': 'Por favor rellena los campos necesarios!'}, status=500)
        else:
            return JsonResponse({'error': 'Usuario no autenticado'}, status=401)
        


def locations_user(request):
    user = request.user
    if user.is_authenticated:
        locations = NoStaffLocation.objects.filter(user=request.user)

        print(locations)


        return render(request, 'users/locations_user.html', {'locations': locations })
    else:
        return redirect('/')


def delete_location(request, id):
    location = NoStaffLocation.objects.get(id=id)
    location.delete()
    return redirect('locations_user')




