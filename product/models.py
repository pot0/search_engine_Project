from django.db import models

# Create your models here.
# class Profile(models.Model):
#     id = models.CharField(max_length=70)
#     photo = 
#     name = models.CharField(max_length=70)

class Product(models.Model):
    product_id = models.CharField(max_length=70)
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

# class OrderModel(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=70)
#     order = Product.id
#     created_at = Product.created_at
#     modified_at = Product.modified_at

