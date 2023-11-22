from django.shortcuts import render
from django.http import JsonResponse
from .models import person, location, phoneNumbers, rol, user

from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


def register_user(request):
    return render(request, 'users/register_user.html')

def validation_register_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)



        if person.objects.filter(email=data['email']).exists():
            return JsonResponse({'status': 'error', 'message': 'El correo eléctronico ya está registrado!'})

        if 'phoneNumbers' in data:
            if phoneNumbers.objects.filter(phoneNumbers=data['phoneNumbers']).exists():
                return JsonResponse({'status': 'error', 'message': 'El número de teléfono ya ha sido registrado!'})


        return JsonResponse({'status': 'success'})
    

    return JsonResponse({'status': 'error'})



def register_user_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)

        existing_rol = rol.objects.get(pk=1)

        if person.objects.filter(email=data['email']).exists():
            return JsonResponse({'status': 'error', 'message': 'El correo eléctronico ya está registrado!'})

        if phoneNumbers.objects.filter(telephoneNumber=data['telephoneNumber']).exists():
            return JsonResponse({'status': 'error', 'message': 'El número de teléfono ya ha sido registrado!'})

        # Procesa los datos según tus modelos
        person_instance = person.objects.create(
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            password=data['password']
        )

        location_instance = location.objects.create(
            person=person_instance,
            adressinput=data['addressInput'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            houseNumber=data['houseNumber'],
            deliveryInstructions=data['text'],
            directionName=data['radio2']
        )

        phone_instance = phoneNumbers.objects.create(
            location=location_instance,
            telephoneNumber=data['telephoneNumber']
        )

        user_instance = user.objects.create(
            person=person_instance,
            location=location_instance,
            number=phone_instance
        )

         # Obtener una lista de los campos que se enviaron con éxito
        successful_fields = [field for field in data.keys()]

        user_instance.rol.add(existing_rol)

        return JsonResponse({'status': 'success', 'successful_fields': successful_fields})
    

    return JsonResponse({'status': 'error'})
