from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import StaffLocation, NoStaffLocation


from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


def register_user(request):
    return render(request, 'users/register_user.html')

def validation_register_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)

        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'status': 'error', 'message': 'El correo electrónico ya está registrado!'})
        

        user_instance = User.objects.create_user(
            
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


