from rest_framework import serializers
from ..models.order import Order

class OrderStatusSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    status= serializers.ChoiceField(choices= Order.Status.choices)
    
    def update(self, instance,validated_data):
        instance.status = validated_data['status']
        instance.save(update_fields=['status', 'updated_at'])
        return instance