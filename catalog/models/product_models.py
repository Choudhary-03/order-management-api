from django.db import models
from .category_models import Category
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    category= models.ForeignKey(Category, on_delete= models.PROTECT, related_name= 'products')
    quantity=models.PositiveIntegerField()
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to = 'catalog/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)