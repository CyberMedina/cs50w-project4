from django.shortcuts import render
import requests
import json
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
import os


load_dotenv()

# Create your views here.


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
