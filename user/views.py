from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import user
from .models import StaffLocation, NoStaffLocation, CustomUser
from django.contrib.auth import logout
from social_django.models import UserSocialAuth


from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


def register_userG(request):

    if request.user.is_authenticated and request.user.is_first_time_Google:

        request.user.is_first_time_Google = False
        request.user.save()

        return render(request, 'users/register_userG.html')
    
    if request.user.is_authenticated:

        return render(request, 'users/register_userG.html')
    
    else:
        return redirect('/')
    




def register_user(request):
    return render(request, 'users/register_user.html')

def validation_register_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)

        if CustomUser.objects.filter(email=data['email']).exists():
            return JsonResponse({'status': 'error', 'message': 'El correo electrónico ya está registrado!'})
        

        user_instance = CustomUser.objects.create_user(
            
            username = data['email'],
            email= data['email'],
            password= data['password'],
            first_name= data['name'],
            last_name=data['lastname']
        )

        user = authenticate(username=data['email'], password=data['password'])
        if user is not None:
            login(request)

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
    return JsonResponse({'status': 'success', 'message' : 'Ha iniciado sesión!'})


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


