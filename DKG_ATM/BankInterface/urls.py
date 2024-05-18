"""
URL configuration for DKG_ATM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.urls import path
from .views import AccountListView, AccountDetailView, WithdrawalView, DepositView, PinChangeView, VerifyPinView, AvailableBalanceView

app_name = 'BankInterface'

urlpatterns = [
    path('verify_pin/', VerifyPinView.as_view(), name='verify_pin'),
    path('available_balance/', AvailableBalanceView.as_view(), name='available_balance'),
    path('withdraw/', WithdrawalView.as_view(), name='withdraw'),
    path('deposit/', DepositView.as_view(), name='deposit'),
    path('pin_change/', PinChangeView.as_view(), name='pin_change'),
    path('accounts/', AccountListView.as_view(), name='account_list'),
    path('accounts/<str:account_number>/', AccountDetailView.as_view(), name='account_detail'),
    path('admin/', admin.site.urls),
]





