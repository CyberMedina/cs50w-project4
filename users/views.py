from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt 

import json

# Create your views here.

def register_user(request):
    return render (request, 'users/register_user.html')


def register_user_API(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)
        
       

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)
