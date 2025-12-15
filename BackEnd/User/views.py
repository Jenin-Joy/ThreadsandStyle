from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Guest.models import tbl_user
from Seller.models import tbl_product,tbl_productcolor,tbl_productsize,tbl_gallery
import json
from django.http import JsonResponse
from django.db.models import F
from django.db.models import Prefetch
# Create your views here.

@csrf_exempt
def profile(request):
    if request.method == "GET":
        data = json.loads(request.body)
        user = tbl_user.objects.get(id=data['uid'])
        return JsonResponse({
            'id': user.id,
            'user_name': user.user_name,
            'user_email': user.user_email,
            'user_doj': user.user_doj,
            'user_contact': user.user_contact,
            'user_gender': user.user_gender,
            'user_photo': str(user.user_photo),
        })
    
@csrf_exempt
def editprofile(request):
    data = json.loads(request.body)
    user = tbl_user.objects.get(id=data['uid'])
    if request.method == "GET":
        return JsonResponse({
            'id': user.id,
            'user_name': user.user_name,
            'user_email': user.user_email,
            'user_contact': user.user_contact,
        })
    if request.method == "PUT":
        user.user_name = data['user_name']
        user.user_email = data['user_email']
        user.user_contact = data['user_contact']
        user.save()
        return JsonResponse({"msg":"Profile Updated..."})
    
@csrf_exempt
def changepassword(request):
    data = json.loads(request.body)
    user = tbl_user.objects.get(id=data['uid'])
    if request.method == "PUT":
        if data['oldpassword'] == user.user_password:
            if data['newpassword'] == data['confirmpassword']:
                user.user_password = data['confirmpassword']
                user.save()
                return JsonResponse({"msg":"Password Updated.."})
            else:
                return JsonResponse({"msg":"Error In Confirm Password.."})
        else:
            return JsonResponse({"msg":"Error In Old Password.."})
        
@csrf_exempt
def viewproduct(request):
    if request.method == "GET":
        product = tbl_product.objects.all().values(
            *[p.name for p in tbl_product._meta.fields],
            brand_name = F('brand__brand_name'),
            subcategory_name = F('subcategory__subcategory_name'),
            category_name = F('subcategory__category__category_name'),
            type_name = F('subcategory__category__type__type_name'),
        )
        for p in product:
            p['color'] = list(tbl_productcolor.objects.filter(product=p['id']).values_list(
                'color__color_name',flat=True
            ))
            p['size'] = list(tbl_productsize.objects.filter(productcolor__product=p['id']).values_list(
                'size__size_name',flat=True
            ))
            p['gallery'] = list(tbl_gallery.objects.filter(productcolor__product=p['id']).values_list(
                'gallery_file', flat=True
            ))
        return JsonResponse({"products":list(product)})