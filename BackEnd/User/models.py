from django.db import models
from Guest.models import tbl_user,tbl_seller, tbl_deliveryboy
from Seller.models import tbl_productsize,tbl_product
from Admin.models import tbl_place
# Create your models here.

class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    seller = models.ForeignKey(tbl_seller, on_delete=models.CASCADE)
    deliveryboy = models.ForeignKey(tbl_deliveryboy, on_delete=models.CASCADE, null=True)

class tbl_cart(models.Model):
    cart_quantity = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    productsize = models.ForeignKey(tbl_productsize, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title = models.CharField(max_length=30)
    complaint_content = models.CharField(max_length=150)
    complaint_reply = models.CharField(max_length=150)
    complaint_status = models.IntegerField(default=0)
    complaint_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    cart = models.ForeignKey(tbl_cart, on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_datetime = models.DateTimeField()
    rating_value = models.CharField(max_length=30)
    rating_content = models.CharField(max_length=150)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)

class tbl_ratingfile(models.Model):
    ratingfile_file = models.FileField(upload_to='Assets/User/Rating/')
    rating = models.ForeignKey(tbl_rating, on_delete=models.CASCADE)

class tbl_useraddress(models.Model):
    useraddress_address = models.CharField(max_length=150)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)

class tbl_wishlist(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)