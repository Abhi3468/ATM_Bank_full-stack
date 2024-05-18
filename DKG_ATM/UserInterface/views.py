from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from . models import UserInterface
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    return render(request, "index.html")

def validate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')  # Decode byte-like object to string
        data = json.loads(data)  # Parse JSON string to Python dictionary

        card_number = data.get('card_number')
        pin = data.get('pin')

        try:
            user = UserInterface.objects.get(card_number=card_number, pin=pin)
            return JsonResponse({'valid': True})
        except UserInterface.DoesNotExist:
            return JsonResponse({'valid': False})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

def next_page(request):
    return render(request, "next_page.html")