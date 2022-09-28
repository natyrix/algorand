from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def index(request):
    return JsonResponse({'success':True})


def check_account(request):
    try:
        if request.method == 'POST':
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})

