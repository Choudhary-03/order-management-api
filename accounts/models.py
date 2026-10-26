from django.db import models

# Create your models here.
class Accounts(models.Model):
    username= models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100, unique=True)
    password= models.CharField(max_length=100, null= False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name