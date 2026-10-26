from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending','Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        SHIPPED = 'shipped' , 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled' , 'Cancelled'
        
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name= 'orders',)
    status= models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Order #{self.pk} - {self.customer}'
