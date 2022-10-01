from distutils.command.upload import upload
from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from api.models import Account, Assets
from django.core.files.storage import FileSystemStorage

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
                    fetched_account = fetched_account.first()
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


def file_upload_and_save_asset(request):
    try:
        if request.method == 'POST':
            myfile = request.FILES['file']
            address = request.POST.get('address')
            asset_id = request.POST.get('asset_id')
            print("VALUES")
            print(myfile)
            print(asset_id)
            print(address)
            fs = FileSystemStorage()
            file_name = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(file_name)
            account = Account.objects.filter(address=address)
            if address and asset_id:
                if account.first():
                    asset_obj = Assets.objects.create(account=account.first(), asset_index=asset_id, image_url=uploaded_file_url)
                    if asset_obj:
                        return JsonResponse({
                            'success':True,
                            "asset":{
                                "id": asset_obj.id,
                                "asset_index": asset_obj.asset_index,
                                "account": asset_obj.account.address,
                                "image_url": asset_obj.image_url,
                            },
                            'message':"Uploaded"
                        })
                    else:
                        return JsonResponse({'success':False,'message':"File upload failed"})
                else:
                    return JsonResponse({'success':False,'message':"Account not found"})
            else:
                return JsonResponse({'success':False,'message':"All fields are required"})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
        
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})


def set_asset_index(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            asset_id = data.get('asset_id')
            asset_index = data.get('asset_index')
            if asset_id and asset_index:
                asset = Assets.objects.filter(id=int(asset_id))
                if asset.first():
                    asset = asset.first()
                    asset.asset_index = asset_index
                    asset.save()
                    return JsonResponse({'success':True,'message':'Updated'})
                else:
                    return JsonResponse({'success':False,'message':'Asset not found'})
            else:
                return JsonResponse({'success':False,'message':'All fields are required'})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})



def get_all_requests(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')
            if address:
                address = str(address).strip()
                fetched_account = Account.objects.filter(address=address)
                if fetched_account and fetched_account[0].is_admin:
                    acounts_list = Account.objects.filter(has_requested=True, request_status=False, is_admin=False)
                    ls = []
                    for acc in acounts_list:
                        ls.append({
                            'id':acc.id,
                            'address': acc.address,
                            'first_name': acc.first_name,
                            'last_name': acc.last_name,
                            'is_admin': acc.is_admin,
                            'request_status': acc.request_status,
                            'has_requested': acc.has_requested,
                        })
                    return JsonResponse({
                        'success': True,
                        'account_list': ls
                    })
                    
                else:
                    return JsonResponse({'success':False,'message':'Account not found' if not fetched_account else 'Access Denied'})
            else:
                return JsonResponse({'success':False,'message':'All fields are required'})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})



def get_all_assets(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')
            if address:
                address = str(address).strip()
                fetched_account = Account.objects.filter(address=address)
                if fetched_account and fetched_account[0].is_admin:
                    assets = Assets.objects.all()
                    ls = []
                    for asset in assets:
                        ls.append({
                            'id': asset.id,
                            'asset_index':asset.asset_index,
                            'asset_status':asset.asset_status,
                            'image_url':f"http://127.0.0.1:8000{asset.image_url}",
                            'account':{
                                'id':asset.account.id,
                                'address': asset.account.address,
                                'first_name': asset.account.first_name,
                                'last_name': asset.account.last_name,
                                'is_admin': asset.account.is_admin,
                                'request_status': asset.account.request_status,
                                'has_requested': asset.account.has_requested,
                            }
                        })
                    return JsonResponse({
                        'success': True,
                        'asset_list': ls
                    })
                    
                else:
                    return JsonResponse({'success':False,'message':'Account not found' if not fetched_account else 'Access Denied'})
            else:
                return JsonResponse({'success':False,'message':'All fields are required'})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})


def get_assets_trainee(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')
            if address:
                address = str(address).strip()
                fetched_account = Account.objects.filter(address=address)
                if fetched_account:
                    fetched_account = fetched_account.first()
                    assets = Assets.objects.filter(account=fetched_account)
                    ls = []
                    for asset in assets:
                        ls.append({
                            'id': asset.id,
                            'asset_index':asset.asset_index,
                            'asset_status':asset.asset_status,
                            'image_url':f"http://127.0.0.1:8000{asset.image_url}",
                            'account':{
                                'id':asset.account.id,
                                'address': asset.account.address,
                                'first_name': asset.account.first_name,
                                'last_name': asset.account.last_name,
                                'is_admin': asset.account.is_admin,
                                'request_status': asset.account.request_status,
                                'has_requested': asset.account.has_requested,
                            }
                        })
                    return JsonResponse({
                        'success': True,
                        'asset_list': ls
                    })
                    
                else:
                    return JsonResponse({'success':False,'message':'Account not found'})
            else:
                return JsonResponse({'success':False,'message':'All fields are required'})
        else:
            return JsonResponse({'success':False,'message':f'method {request.method} not allowed'})
    except Exception as e:
        return JsonResponse({'success':False,'message':str(e)})