from django.shortcuts import render
from Seller.models import *
from Admin.models import tbl_brand, tbl_subcategory
from Guest.models import tbl_seller
import json
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
# Create your views here.

@csrf_exempt
def profile(request):
    if request.method == "GET":
        data = json.loads(request.body)
        seller = tbl_seller.objects.get(id=data['sid'])
        return JsonResponse({
            'id': seller.id,
            'seller_name': seller.seller_name,
            'seller_email': seller.seller_email,
            'seller_address': seller.seller_address,
            'seller_slogan': seller.seller_slogan,
            'seller_logo': str(seller.seller_logo),
            'place_name': seller.place.place_name,
            'district_name': seller.place.district.district_name,
        })
    
@csrf_exempt
def editprofile(request):
    data = json.loads(request.body)
    seller = tbl_seller.objects.get(id=data['sid'])
    if request.method == "GET":
        return JsonResponse({
            'id': seller.id,
            'seller_name': seller.seller_name,
            'seller_email': seller.seller_email,
            'seller_address': seller.seller_address,
            'seller_slogan': seller.seller_slogan,
        })
    if request.method == "PUT":
        seller.seller_name = data['seller_name']
        seller.seller_email = data['seller_email']
        seller.seller_address = data['seller_address']
        seller.seller_slogan = data['seller_slogan']
        seller.save()
        return JsonResponse({"msg":"Profile Updated..."})
    
@csrf_exempt
def changepassword(request):
    data = json.loads(request.body)
    seller = tbl_seller.objects.get(id=data['sid'])
    if request.method == "PUT":
        if data['oldpassword'] == seller.seller_password:
            if data['newpassword'] == data['confirmpassword']:
                seller.seller_password = data['confirmpassword']
                seller.save()
                return JsonResponse({"msg":"Password Updated.."})
            else:
                return JsonResponse({"msg":"Error In Confirm Password.."})
        else:
            return JsonResponse({"msg":"Error In Old Password.."})

@csrf_exempt
def product(request):
    data = json.loads(request.body)
    if request.method == "POST":
        tbl_product.objects.create(
            product_name = data['product_name'],
            product_details = data['product_details'],
            brand = tbl_brand.objects.get(id=data['brand_id']),
            subcategory = tbl_subcategory.objects.get(id=data['subcategory_id']),
            seller = tbl_seller.objects.get(id=data['seller_id'])
        )
        return JsonResponse({"msg":"Product Added.."})
    if request.method == "GET":
        product = tbl_product.objects.filter(seller=data['seller_id']).values(
            'id',
            'product_name',
            'product_details',
            'product_status',
            brand_name=F('brand__brand_name'),
            subcategory_name=F('subcategory__subcategory_name'),
            category_name=F('subcategory__category__category_name'),
            type_name=F('subcategory__category__type__type_name')
        )
        return JsonResponse({"products":list(product)})
    
@csrf_exempt
def handleProduct(request, id):
    if request.method == "DELETE":
        tbl_product.objects.get(id=id).delete()
        return JsonResponse({"msg":"Product Deleted..."})
    
@csrf_exempt
def productcolor(request):
    data = json.loads(request.body)
    if request.method == "POST":
        tbl_productcolor.objects.create(
            product=tbl_product.objects.get(id=data['product_id']),
            color = tbl_color.objects.get(id=data['color_id'])
        )
        return JsonResponse({"msg":"Product Color Added..."})
    if request.method == "GET":
        productcolor = tbl_productcolor.objects.filter(product=data['product_id']).values(
            'id', 'product', color_name = F('color__color_name'), 
        )
        return JsonResponse({"productcolor":list(productcolor)})
    
@csrf_exempt
def handleProductcolor(request, id):
    productcolor = tbl_productcolor.objects.get(id=id)
    if request.method == "DELETE":
        productcolor.delete()
        return JsonResponse({"msg":"Product Color Delete..."})
    if request.method == "GET":
        return JsonResponse({
            "id" : productcolor.id,
            "color_id" : productcolor.color.id
        })
    if request.method == "PUT":
        data = json.loads(request.body)
        productcolor.color = tbl_color.objects.get(id=data['color_id'])
        productcolor.save()
        return JsonResponse({"msg":"Product Color Updated..."})
    
@csrf_exempt
def productsize(request):
    data = json.loads(request.body)
    if request.method == "POST":
        tbl_productsize.objects.create(
            productcolor = tbl_productcolor.objects.get(id=data['productcolor_id']),
            size = tbl_size.objects.get(id=data['size_id']),
            product_amount = data['product_amount']
        )
        return JsonResponse({"msg":"Product Size Added..."})
    if request.method == "GET":
        productsize = tbl_productsize.objects.filter(productcolor=data['productcolor_id']).values(
            'id',
            'product_amount',
            size_name = F('size__size_name'),
            productcolor_name = F('productcolor__color__color_name')
        )
        return JsonResponse({"productsize":list(productsize)})
    
@csrf_exempt
def handleProductsize(request, id):
    productsize = tbl_productsize.objects.get(id=id)
    if request.method == "DELETE":
        productsize.delete()
        return JsonResponse({"msg":"Product Size Deleted.."})
    if request.method == "GET":
        return JsonResponse({
            "id" : productsize.id,
            "size_id" : productsize.size.id,
            "product_amount" : productsize.product_amount
        })
    if request.method == "PUT":
        data = json.loads(request.body)
        productsize.size = tbl_size.objects.get(id=data['size_id'])
        productsize.product_amount = data['product_amount']
        productsize.save()
        return JsonResponse({"msg":"Product Size Updated.."})
    
@csrf_exempt
def stock(request):
    data = json.loads(request.body)
    if request.method == "POST":
        tbl_stock.objects.create(
            productsize = tbl_productsize.objects.get(id=data['productsize_id']),
            stock_count = data['stock_count']
        )
        return JsonResponse({"msg":"Stock Added..."})
    if request.method == "GET":
        stock = tbl_stock.objects.filter(productsize=data['productsize_id']).values(
            'id',
            'stock_count',
            productsize_name = F('productsize__size__size_name')
        )
        return JsonResponse({"stocks":list(stock)})
    
@csrf_exempt
def handleStock(request, id):
    stock = tbl_stock.objects.get(id=id)
    if request.method == "DELETE":
        stock.delete()
        return JsonResponse({"msg":"Stock Deleted..."})
    
@csrf_exempt
def gallery(request):
    if request.method == "POST":
        files = request.FILES.getlist('gallery_file')
        for file in files:
            tbl_gallery.objects.create(
                gallery_file = file,
                productcolor = tbl_productcolor.objects.get(id=request.POST.get('productcolor_id'))
            )
        return JsonResponse({"msg":"File Added..."})
    if request.method == "GET":
        data = json.loads(request.body)
        gallery = tbl_gallery.objects.filter(productcolor=data['productcolor_id']).values(
            'id',
            'gallery_file',
            productcolor_name = F('productcolor__color__color_name')
        )
        return JsonResponse({"gallery":list(gallery)})
    
@csrf_exempt
def handleGallery(request, id):
    if request.method == "DELETE":
        tbl_gallery.objects.get(id=id).delete()
        return JsonResponse({"msg":"Gallery Deleted..."})