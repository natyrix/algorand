from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from api.models import Account


def index(request):
    return JsonResponse({'success':True})


def check_account(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')
            if address:
                address = str(address).strip()
                fetched_account = Account.objects.filter(address=address)
                if fetched_account:
                    return JsonResponse({
                        'success':True,
                        'account': {
                            'address': fetched_account.address,
                            'first_name': fetched_account.first_name,
                            'last_name': fetched_account.last_name,
                            'is_admin': fetched_account.is_admin,
                        }
                    })
                else:
                    return JsonResponse({'success':False,'message':'No account found', 'status_code':111})
            else:
                return JsonResponse({'success':False,'message':'Address is required'})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})


def create_account(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            is_admin = data.get('is_admin')
            if address and first_name and last_name:
                address = str(address).strip()
                fetched_address = Account.objects.filter(address=address)
                if not fetched_address:
                    first_name = str(first_name).strip()
                    last_name = str(last_name).strip()
                    adm = False
                    if is_admin:
                        adm = is_admin
                    account = Account.objects.create(address=address, first_name=first_name, last_name=last_name, is_admin=adm)
                    return JsonResponse({
                        'success':True,
                        'message':'Account create',
                        'account': {
                            'address': account.address,
                            'first_name': account.first_name,
                            'last_name': account.last_name,
                            'is_admin': account.is_admin,
                        }
                    })
                else:
                    return JsonResponse({'success':False,'message':'Address already registered'})
            else:
                return JsonResponse({'success':False,'message':'All fields are required'})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})

