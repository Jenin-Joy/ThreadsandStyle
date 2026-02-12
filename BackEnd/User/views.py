from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from Guest.models import tbl_user
from User.models import *
from Seller.models import tbl_product,tbl_productcolor,tbl_productsize,tbl_gallery,tbl_stock
import json
from django.http import JsonResponse
from django.db.models import F
# Create your views here.


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
        
def viewproduct(request):
    if request.method == "GET":
        product = tbl_product.objects.all().values()
        for p in product:
            p['gallery'] = list(tbl_gallery.objects.filter(productcolor__product=p['id']).values_list(
                'gallery_file', flat=True
            ))
        return JsonResponse({"products":list(product)}) 
        
def viewproductdetails(request, id):
    if request.method == "GET":
        product = tbl_product.objects.filter(id=id).values(
            *[p.name for p in tbl_product._meta.fields],
            brand_name = F('brand__brand_name'),
            subcategory_name = F('subcategory__subcategory_name'),
            category_name = F('subcategory__category__category_name'),
            type_name = F('subcategory__category__type__type_name'),
        ).first()
        product['color'] = list(tbl_productcolor.objects.filter(product=product['id']).values_list(
            'color__color_name',flat=True
        ))
        product['size'] = list(tbl_productsize.objects.filter(productcolor__product=product['id']).values_list(
            'size__size_name',flat=True
        ))
        product['gallery'] = list(tbl_gallery.objects.filter(productcolor__product=product['id']).values_list(
            'gallery_file', flat=True
        ))
        product['stock'] = list(tbl_stock.objects.filter(productsize__productcolor__product=product['id']).aggregate(total_stock=Sum('stock_count')).values())
        return JsonResponse({"products":product})
    
def addtocart(request):
    if request.method == "GET":
        data = json.loads(request.body)
        productsize_data = tbl_productsize.objects.get(id=data['productsizeid'])
        booking_count = tbl_booking.objects.filter(booking_status=0, user=data['uid'], seller=data['sellerid']).count()
        if booking_count > 0:
            bookingdata = tbl_booking.objects.get(booking_status=0, user=data['uid'], seller=data['sellerid'])
            cart_count = tbl_cart.objects.filter(booking=bookingdata, productsize=data['productsizeid']).count()
            if cart_count > 0:
                return JsonResponse({"msg":"Product Already in cart..."})
            else:
                tbl_cart.objects.create(booking=bookingdata,productsize = productsize_data)
                return JsonResponse({"msg":"Product Added to cart..."})
        else:
            book = tbl_booking.objects.create(user=tbl_user.objects.get(id=data['uid']),seller=tbl_seller.objects.get(id=productsize_data.productcolor.product.seller.id))
            tbl_cart.objects.create(booking=book,productsize=productsize_data)
            return JsonResponse({"msg":"Product Added to cart..."})
        
def mycart(request):
    if request.method == "GET":
        data = json.loads(request.body)
        cart = tbl_cart.objects.filter(booking__booking_status=0, booking__user=data['uid'], booking__seller=data['sellerid']).values(
            *[c.name for c in tbl_cart._meta.fields],
            product_name = F('productsize__productcolor__product__product_name'),
            product_price = F('productsize__product_amount'),
            color_name = F('productsize__productcolor__color__color_name'),
            size_name = F('productsize__size__size_name'),
            color_id = F('productsize__productcolor__id')
        )
        for i in cart:
            total_stock = tbl_stock.objects.filter(productsize=i['productsize']).aggregate(total_stock=Sum('stock_count'))['total_stock'] or 0
            buyed_stock = tbl_cart.objects.filter(productsize=i['productsize'], booking__booking_status__gt=0).aggregate(buyed_stock=Sum('cart_quantity'))['buyed_stock'] or 0
            balance_stock = total_stock - buyed_stock
            i['total_stock'] = balance_stock
            i['product_image'] = list(tbl_gallery.objects.filter(productcolor=i['color_id']).values_list('gallery_file', flat=True))
        return JsonResponse({"cart":list(cart)})
    
@csrf_exempt
def updatecart(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        tbl_cart.objects.get(id=data['cartid']).delete()
        return JsonResponse({"msg":"Product Removed from cart..."})
    if request.method == "PUT":
        tbl_cart.objects.get(id=data['cartid']).update(cart_quantity = int(data['quantity']))
        return JsonResponse({"msg":"Quantity Updated..."})