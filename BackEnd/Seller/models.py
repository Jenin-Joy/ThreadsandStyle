from django.db import models
from Guest.models import tbl_seller
from Admin.models import tbl_subcategory,tbl_type,tbl_brand,tbl_color,tbl_size
# Create your models here.

class tbl_product(models.Model):
    product_name = models.CharField(max_length=30)
    product_details = models.CharField(max_length=150)
    product_status = models.IntegerField(default=0)
    brand = models.ForeignKey(tbl_brand, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
    seller = models.ForeignKey(tbl_seller, on_delete=models.CASCADE)

class tbl_productcolor(models.Model):
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    color = models.ForeignKey(tbl_color, on_delete=models.CASCADE)

class tbl_productsize(models.Model):
    productcolor = models.ForeignKey(tbl_productcolor, on_delete=models.CASCADE)
    size = models.ForeignKey(tbl_size, on_delete=models.CASCADE)
    product_amount = models.CharField(max_length=30)

class tbl_stock(models.Model):
    stock_date = models.DateField(auto_now_add=True)
    stock_count = models.CharField(max_length=30)
    productsize = models.ForeignKey(tbl_productsize, on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_file = models.FileField(upload_to='Assets/Seller/Product/')
    productcolor = models.ForeignKey(tbl_productcolor, on_delete=models.CASCADE)