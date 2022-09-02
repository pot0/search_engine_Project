from django.db import models

# Create your models here.
# class Profile(models.Model):
#     id = models.CharField(max_length=70)
#     photo = 
#     name = models.CharField(max_length=70)

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# class OrderModel(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=70)
#     order = Product.id
#     created_at = Product.created_at
#     modified_at = Product.modified_at

