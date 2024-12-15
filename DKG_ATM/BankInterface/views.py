from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from decimal import Decimal
import json
from .models import Account, WithdrawalHistory, DepositHistory

@method_decorator(csrf_exempt, name='dispatch')
class AccountListView(View):
    def get(self, request):
        accounts = Account.objects.all().values()
        return JsonResponse(list(accounts), safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        account = Account.objects.create(
            card_number=data['card_number'],
            card_pin=data['card_pin'],
            balance=data['balance']
        )
        return JsonResponse({'card_number': account.card_number}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class AccountDetailView(View):
    def get(self, request, card_number):
        account = get_object_or_404(Account, card_number=card_number)
        return JsonResponse({
            'card_number': account.card_number,
            'card_pin': account.card_pin,
            'balance': account.balance
        })

    def put(self, request, card_number):
        data = json.loads(request.body)
        account = get_object_or_404(Account,card_number=card_number)
        account.card_number = data.get('card_number', account.card_number)
        account.card_pin = data.get('card_pin', account.card_pin)
        account.balance = data.get('balance', account.balance)
        account.save()
        return JsonResponse({'card_number': account.card_number})

    def delete(self, request, card_number):
        account = get_object_or_404(Account, card_number=card_number)
        account.delete()
        return JsonResponse({'message': 'Account deleted successfully'}, status=204)

@method_decorator(csrf_exempt, name='dispatch')
class WithdrawalView(View):
    def post(self, request):
        data = json.loads(request.body)
        card_number = data['card_number']
        amount = Decimal(data.get('amount'))
        account = get_object_or_404(Account, card_number=card_number)
        if account.balance < amount:
            return JsonResponse({'error': 'Insufficient funds'}, status=400)
        account.balance -= amount
        account.save()
        WithdrawalHistory.objects.create(account=account, amount=amount)
        return JsonResponse({'message': 'Withdrawal successful', 'new_balance': account.balance})

@method_decorator(csrf_exempt, name='dispatch')
class DepositView(View):
    def post(self, request):
        data = json.loads(request.body)
        card_number = data['card_number']
        amount = Decimal(data.get('amount'))    
        account = get_object_or_404(Account, card_number=card_number)
        account.balance += amount
        account.save()
        DepositHistory.objects.create(account=account, amount=amount)
        return JsonResponse({'message': 'Deposit successful', 'new_balance': account.balance})

@method_decorator(csrf_exempt, name='dispatch')
class PinChangeView(View):
    def post(self, request):
        data = json.loads(request.body)
        card_number = data['card_number']
        new_pin = data['new_pin']
        account = get_object_or_404(Account, card_number=card_number)
        account.card_pin = new_pin
        account.save()
        return JsonResponse({'message': 'PIN changed successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class VerifyPinView(View):
    def post(self, request):
        data = json.loads(request.body)
        card_pin = data.get('card_pin')
        try:
            account = Account.objects.get(card_pin=card_pin)
            return JsonResponse({'message': 'Verified', 'card_number': account.card_number})
        except Account.DoesNotExist:
            return JsonResponse({'message': 'Invalid PIN'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class AvailableBalanceView(View):
    def post(self, request):
        data = json.loads(request.body)
        card_number = data.get('card_number')
        try:
            account = Account.objects.get(card_number=card_number)
            return JsonResponse({'balance': account.balance})
        except Account.DoesNotExist:
            return JsonResponse({'error': f"No Account found for card number {card_number}"}, status=400)
