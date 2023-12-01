from django.shortcuts import render

# Create your views here.

def homeUser(request):
    return render(request, 'homeUser/index.html')
