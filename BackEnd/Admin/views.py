from django.shortcuts import render
from Admin.models import *
from Guest.models import tbl_seller, tbl_deliveryboy
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db.models import F
# Create your views here.

@csrf_exempt
def district(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tbl_district.objects.create(district_name=data['district_name'])
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        district = tbl_district.objects.all()
        return JsonResponse({'district': list(district.values())})

@csrf_exempt
def handleDistrict(request, id):
    district = tbl_district.objects.get(id=id)
    if request.method == 'DELETE':
        district.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({"id":district.id,"district_name":district.district_name})
    if request.method == 'PUT':
        data = json.loads(request.body)
        district.district_name = data['district_name']
        district.save()
        return JsonResponse({'status': 'Data Updated'})
    
@csrf_exempt
def place(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        district = tbl_district.objects.get(id=data['district_id'])
        tbl_place.objects.create(place_name=data['place_name'], district=district)
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        place = tbl_place.objects.values(
            'id', 'place_name', 'district', district_name=F('district__district_name')
        )
        return JsonResponse({'places': list(place)})
    
@csrf_exempt
def handlePlace(request,id):
    place = tbl_place.objects.get(id=id)
    if request.method == 'DELETE':
        place.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({'id':place.id,
                             'place_name':place.place_name,
                             "district":place.district.id,
                            })
    if request.method == 'PUT':
        data = json.loads(request.body)
        place.district = tbl_district.objects.get(id=data['district_id'])
        place.place_name=data['place_name']
        place.save()
        return JsonResponse({'status': 'Data Updated'})
    
@csrf_exempt
def brand(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tbl_brand.objects.create(brand_name=data['brand_name'])
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        brand = tbl_brand.objects.all()
        return JsonResponse({'brand': list(brand.values())})

@csrf_exempt
def handleBrand(request, id):
    brand = tbl_brand.objects.get(id=id)
    if request.method == 'DELETE':
        brand.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({"id":brand.id,"brand_name":brand.brand_name})
    if request.method == 'PUT':
        data = json.loads(request.body)
        brand.brand_name = data['brand_name']
        brand.save()
        return JsonResponse({'status': 'Data Updated'})

@csrf_exempt
def color(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tbl_color.objects.create(color_name=data['color_name'])
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        color = tbl_color.objects.all()
        return JsonResponse({'color': list(color.values())})

@csrf_exempt
def handleColor(request, id):
    color = tbl_color.objects.get(id=id)
    if request.method == 'DELETE':
        color.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({"id":color.id,"color_name":color.color_name})
    if request.method == 'PUT':
        data = json.loads(request.body)
        color.color_name = data['color_name']
        color.save()
        return JsonResponse({'status': 'Data Updated'})
    
@csrf_exempt
def size(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tbl_size.objects.create(size_name=data['size_name'])
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        size = tbl_size.objects.all()
        return JsonResponse({'size': list(size.values())})

@csrf_exempt
def handleSize(request, id):
    size = tbl_size.objects.get(id=id)
    if request.method == 'DELETE':
        size.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({"id":size.id,"size_name":size.size_name})
    if request.method == 'PUT':
        data = json.loads(request.body)
        size.size_name = data['size_name']
        size.save()
        return JsonResponse({'status': 'Data Updated'})
    
@csrf_exempt
def type(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tbl_type.objects.create(type_name=data['type_name'])
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        type = tbl_type.objects.all()
        return JsonResponse({'type': list(type.values())})

@csrf_exempt
def handleType(request, id):
    type = tbl_type.objects.get(id=id)
    if request.method == 'DELETE':
        type.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({"id":type.id,"type_name":type.type_name})
    if request.method == 'PUT':
        data = json.loads(request.body)
        type.type_name = data['type_name']
        type.save()
        return JsonResponse({'status': 'Data Updated'})

@csrf_exempt
def category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        type = tbl_type.objects.get(id=data['type_id'])
        tbl_category.objects.create(category_name=data['category_name'], type=type)
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        category = tbl_category.objects.values(
            'id', 'category_name', 'type', type_name=F('type__type_name')
        )
        return JsonResponse({'categorys': list(category)})
    
@csrf_exempt
def handleCategory(request,id):
    category = tbl_category.objects.get(id=id)
    if request.method == 'DELETE':
        category.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({'id':category.id,
                             'category_name':category.category_name,
                             "type":category.type.id,
                            })
    if request.method == 'PUT':
        data = json.loads(request.body)
        category.type = tbl_type.objects.get(id=data['type_id'])
        category.category_name=data['category_name']
        category.save()
        return JsonResponse({'status': 'Data Updated'})
    
@csrf_exempt
def subcategory(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        category = tbl_category.objects.get(id=data['category_id'])
        tbl_subcategory.objects.create(subcategory_name=data['subcategory_name'], category=category)
        return JsonResponse({'status': 'Data Inserted'})
    if request.method == 'GET':
        subcategory = tbl_subcategory.objects.values(
            'id', 'subcategory_name', 'category', category_name=F('category__category_name'), type_name=F('category__type__type_name')
        )
        return JsonResponse({'subcategorys': list(subcategory)})
    
@csrf_exempt
def handleSubcategory(request,id):
    subcategory = tbl_subcategory.objects.get(id=id)
    if request.method == 'DELETE':
        subcategory.delete()
        return JsonResponse({'status': 'Data Deleted'})
    if request.method == 'GET':
        return JsonResponse({'id':subcategory.id,
                             'subcategory_name':subcategory.subcategory_name,
                             "category":subcategory.category.id,
                            })
    if request.method == 'PUT':
        data = json.loads(request.body)
        subcategory.category = tbl_category.objects.get(id=data['category_id'])
        subcategory.subcategory_name=data['subcategory_name']
        subcategory.save()
        return JsonResponse({'status': 'Data Updated'})
    
@csrf_exempt
def sellerverification(request):
    if request.method == "GET":
        seller_fields = [f.name for f in tbl_seller._meta.fields]
        newseller = tbl_seller.objects.filter(seller_status=0).values(
            *seller_fields,
            place_name=F('place__place_name'),
            district_name=F('place__district__district_name'),
        )
        acceptedseller = tbl_seller.objects.filter(seller_status=1).values(
            *seller_fields,
            place_name = F('place__place_name'),
            district_name = F('place__district__district_name')
        )
        rejectedseller = tbl_seller.objects.filter(seller_status=2).values(
            *seller_fields,
            place_name = F('place__place_name'),
            district_name = F('place__district__district_name')
        )
        return JsonResponse({
            "newseller":list(newseller),
            "acceptedseller":list(acceptedseller),
            "rejectedseller":list(rejectedseller)
            })
    
@csrf_exempt
def handleSellerverification(request, id, status):
    seller = tbl_seller.objects.get(id=id)
    if request.method == "PUT":
        seller.seller_status = status
        seller.save()
        messages = { 1: "Seller Accepted ✅", 2: "Seller Rejected ❌" } 
        msg = messages.get(int(status), "Status Updated.")
        return JsonResponse({"msg":msg})
    
@csrf_exempt
def deliveryboyverification(request):
    if request.method == "GET":
        deliveryboy_fields = [f.name for f in tbl_deliveryboy._meta.fields]
        newdeliveryboy = tbl_deliveryboy.objects.filter(deliveryboy_status=0).values(
            *deliveryboy_fields,
            place_name = F('place__place_name'),
            district_name = F('place__district__district_name')
        )
        accepteddeliveryboy = tbl_deliveryboy.objects.filter(deliveryboy_status=1).values(
            *deliveryboy_fields,
            place_name = F('place__place_name'),
            district_name = F('place__district__district_name')
        )
        rejecteddeliveryboy = tbl_deliveryboy.objects.filter(deliveryboy_status=2).values(
            *deliveryboy_fields,
            place_name = F('place__place_name'),
            district_name = F('place__district__district_name')
        )
        return JsonResponse({
            "newdeliveryboy":list(newdeliveryboy),
            "accepteddeliveryboy":list(accepteddeliveryboy),
            "rejecteddeliveryboy":list(rejecteddeliveryboy)
            })
    
@csrf_exempt
def handleDeliveryboyverification(request, id, status):
    deliveryboy = tbl_deliveryboy.objects.get(id=id)
    if request.method == "PUT":
        deliveryboy.deliveryboy_status = status
        deliveryboy.save()
        messages = { 1: "Deliveryboy Accepted ✅", 2: "Deliveryboy Rejected ❌" } 
        msg = messages.get(int(status), "Status Updated.")
        return JsonResponse({"msg":msg})