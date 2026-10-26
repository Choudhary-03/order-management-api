from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from ..models.order import Order
from ..models.order_items import OrderItem  
from .order_item_serializers import OrderItemSerializer


class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(source='id', read_only = True)
    customer_name= serializers.SerializerMethodField()
    status= serializers.ChoiceField(choices=Order.Status.choices, read_only=True)
    total_amount = serializers.DecimalField(max_digits=12, decimal_places=2, read_only = True)
    items = OrderItemSerializer(many = True)
    created_at=serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)
    
    def get_customer_name(self, obj):
        user= obj.customer
        return user.username
    
    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError('an order must contain at least one item.')
        
        products=[]
        for item in items:
            if item['product'] in products:
                raise serializers.ValidationError('Each product may appear only once per order.')
            products.append(item['product'])
            
        return items

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        customer=validated_data.pop('customer')
        order = Order.objects.create(customer= customer)
        
        total= Decimal('0')
        order_items = []
        for item in items_data:
            product = item['product']
            quantity= item['quantity']
            
            if product.quantity < quantity:
                raise serializers.ValidationError(
                f'Only {product.quantity} of "{product.name}" in stock.')

            # 2. Reduce stock
            product.quantity -= quantity
            product.save()
                
            
            unit_price= product.unit_price
            total += unit_price *quantity
            order_items.append(
                OrderItem(
                    order=order,
                    product=product,
                    quantity= quantity,
                    unit_price= unit_price,
                )
            )
        
        OrderItem.objects.bulk_create(order_items)
        
        order.total_amount=total
        order.save(update_fields=['total_amount', 'updated_at'])
        return order
    
    def update(self, instance, validated_data):
        raise serializers.ValidationError('Order cannot be modified after creation.')
