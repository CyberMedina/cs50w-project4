from django.shortcuts import render
from user.models import NoStaffLocation
import requests
import json
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
import os


load_dotenv()

# Create your views here.



def orders(request):
    carrito = request.session.get('carrito', {})
    print(carrito)

    # Calcular el total
    total = sum(float(producto['precio']) * producto['cantidad'] for producto in carrito.values())

    locations = None
    if request.user.is_authenticated:
        # Get the NoStaffLocation objects for the authenticated user
        locations = NoStaffLocation.objects.filter(user=request.user)

    if request.method == 'POST':
        print("Entró al POST")
        # Your existing POST method code here...

    return render(request, 'orders/orders.html', {'carrito': carrito, 'total': total, 'locations': locations})

@csrf_exempt
def pruebitaWhatsapp(request):

    whatsappApiKey = os.getenv("WHATSAPP_API_KEY")
    NameDestination = 'Jhonatan Medina'
    DestinationNumber = '50581719517'
    TotalOrder = 'C$ 2,000 córdobas'

    if request.method == 'POST':

        url = f'https://graph.facebook.com/v17.0/{whatsappApiKey}/messages'
        headers = {
            'Authorization': 'Bearer EABhDdHV4cOoBOzXcZBZCjYhRXhlJlRd6yJiKR1BAm8fq2adZCsbzqdSBAU3UwgrarF0oQPAcGQDBrwWc4A4u70H2r8tsCItMXFSDCo2bPN2SUApeNU0IXu6C7Xclno8VWVydQZBDz73zRUqA1XEfGH7rMZCMwt6DrSQqJjtWnV3CuCeFNJAQ2Ky9dCzrisnvs6SM1W0nvrkgspU5vFD0hZBs3eQYoiRlWzPV6ZCTN8bQUsZD',
            'Content-Type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": DestinationNumber,
            "type": "template",
            "template": {
                "name": "envio_orden",
                "language": {
                    "code": "es_mx",
                    "policy": "deterministic"
                },
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": NameDestination
                            },
                            {
                                "type": "text",
                                "text": TotalOrder
                            }
                        ]
                    }
                ]
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        print(response.text)
    

    return render(request, 'orders/pruebitaWhatsapp.html')
