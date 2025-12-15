from django.db import models
from Admin.models import tbl_place
# Create your models here.

class tbl_seller(models.Model):
    seller_name = models.CharField(max_length=30)
    seller_email = models.CharField(max_length=30)
    seller_password = models.CharField(max_length=30)
    seller_address = models.CharField(max_length=150)
    seller_slogan = models.CharField(max_length=100)
    seller_status = models.IntegerField(default=0)
    seller_photo = models.FileField(upload_to='Assets/Seller/Photo/')
    seller_proof = models.FileField(upload_to='Assets/Seller/Proof/')
    seller_logo = models.FileField(upload_to='Assets/Seller/Logo/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)

class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_contact = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    user_status = models.IntegerField(default=0)
    user_doj = models.DateField(auto_now_add=True)
    user_gender = models.CharField(max_length=30)
    user_photo = models.FileField(upload_to='Assets/User/Photo/')

class tbl_deliveryboy(models.Model):
    deliveryboy_name = models.CharField(max_length=30)
    deliveryboy_email = models.CharField(max_length=30)
    deliveryboy_password = models.CharField(max_length=30)
    deliveryboy_contact = models.CharField(max_length=30)
    deliveryboy_status = models.IntegerField(default=0)
    deliveryboy_idproof = models.FileField(upload_to='Assets/Deliveryboy/Idproof/')
    deliveryboy_licence = models.FileField(upload_to='Assets/Deliveryboy/Licence/')
    deliveryboy_photo = models.FileField(upload_to='Assets/Deliveryboy/Photo/')
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)