from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from BankInterface.models import Account  # Import the Account model
from .models import UserInterface
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
            account = Account.objects.get(card_number=card_number, card_pin=pin)
            user = UserInterface.objects.get(account=account)
            return JsonResponse({'valid': True})
        except (Account.DoesNotExist, UserInterface.DoesNotExist):
            return JsonResponse({'valid': False, 'message': 'USER NOT EXISTS'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
def next_page(request):
    return render(request, "next_page.html")
