from django.shortcuts import render
from Guest.models import *
from Admin.models import tbl_place, tbl_admin
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db.models import F
# Create your views here.

@csrf_exempt
def user(request):
    if request.method == "POST":
        tbl_user.objects.create(
            user_name = request.POST.get('user_name'),
            user_email = request.POST.get('user_email'),
            user_contact = request.POST.get('user_contact'),
            user_password = request.POST.get('user_password'),
            user_gender = request.POST.get('user_gender'),
            user_photo = request.FILES.get('user_photo')
        )
        return JsonResponse({"msg":"Registred Sucessfully..."})

@csrf_exempt
def seller(request):
    if request.method == "POST":
        tbl_seller.objects.create(
            seller_name = request.POST.get('seller_name'),
            seller_email = request.POST.get('seller_email'),
            seller_password = request.POST.get('seller_password'),
            seller_address = request.POST.get('seller_address'),
            seller_slogan = request.POST.get('seller_slogan'),
            seller_photo = request.FILES.get('seller_photo'),
            seller_proof = request.FILES.get('seller_proof'),
            seller_logo = request.FILES.get('seller_logo'),
            place = tbl_place.objects.get(id=request.POST.get('place_id')),
        )
        return JsonResponse({"msg":"Registred Sucessfully..."})
    
@csrf_exempt
def deliveryboy(request):
    if request.method == "POST":
        tbl_deliveryboy.objects.create(
            deliveryboy_name = request.POST.get('deliveryboy_name'),
            deliveryboy_email = request.POST.get('deliveryboy_email'),
            deliveryboy_password = request.POST.get('deliveryboy_password'),
            deliveryboy_contact = request.POST.get('deliveryboy_contact'),
            deliveryboy_idproof = request.FILES.get('deliveryboy_idproof'),
            deliveryboy_licence = request.FILES.get('deliveryboy_licence'),
            deliveryboy_photo = request.FILES.get('deliveryboy_photo'),
            place = tbl_place.objects.get(id=request.POST.get('place_id')),
        )
        return JsonResponse({"msg":"Registred Sucessfully..."})
    
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
        deliveryboycount = tbl_deliveryboy.objects.filter(deliveryboy_email=email, deliveryboy_password=password).count()
        sellercount = tbl_seller.objects.filter(seller_email=email, seller_password=password).count()

        if admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            token = {
                "aid": admin.id,
                "aname" : admin.admin_name
            }
            return JsonResponse(token)
        elif usercount > 0:
            user = tbl_user.objects.get(user_email=email,user_password=password)
            token = {
                "uid": user.id,
                "uname" : user.user_name
            }
            return JsonResponse(token)
        elif deliveryboycount > 0:
            deliveryboy = tbl_deliveryboy.objects.get(deliveryboy_email=email, deliveryboy_password=password)
            if deliveryboy.deliveryboy_status == 0:
                return JsonResponse({"msg":"Account Verification Pending..."})
            elif deliveryboy.deliveryboy_status == 2:
                return JsonResponse({"msg":"Account Verification Rejected..."})
            else:
                token = {
                    "did": deliveryboy.id,
                    "dname" : deliveryboy.deliveryboy_name
                }
                return JsonResponse(token)
        elif sellercount > 0:
            seller = tbl_seller.objects.get(seller_email=email, seller_password=password)
            if seller.seller_status == 0:
                return JsonResponse({"msg":"Account Verification Pending..."})
            elif seller.seller_status == 2:
                return JsonResponse({"msg":"Account Verification Rejected..."})
            else:
                token = {
                    "sid": seller.id,
                    "sname" : seller.seller_name
                }
                return JsonResponse(token)
        else:
            return JsonResponse({"msg":"Invalid Email Or Password..."})