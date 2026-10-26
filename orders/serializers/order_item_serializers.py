from rest_framework import serializers
from catalog.models import Product
from ..models.order_items import OrderItem 


class OrderItemSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    product=serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),write_only =True)
    product_name = serializers.CharField(source= 'product.name', read_only=True)
    quantity= serializers.IntegerField(min_value=1)
    unit_price= serializers.DecimalField(max_digits=10,decimal_places=2,read_only=True)
    subtotal= serializers. DecimalField(max_digits=12, decimal_places=2,read_only =True)
    
