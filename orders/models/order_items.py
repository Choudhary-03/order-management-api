from django.db import models
from catalog.models import Product
from .order import Order

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product= models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity= models.PositiveIntegerField()
    unit_price = models. DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        constraints = [

            models.CheckConstraint(condition= models.Q(quantity__gt=0),name='orderitem_quantity_gt_0')
            
           ]
    
    @property
    def subtotal(self):
        return self.quantity*self.unit_price
    
    def __str__(self):
        return f'{self.quantity} x {self.product}'
        