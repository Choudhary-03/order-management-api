from django.db import models
from django.conf import settings 

# Create your models here.
class Customer(models.Model):
    user= models. OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='customer_profile')
    
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=100, unique=True)
    address=models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'