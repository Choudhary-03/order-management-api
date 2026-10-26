from rest_framework import serializers
from .product_serializers import ProductSerializer


class ProductPatchSerializer(ProductSerializer):
    name = serializers.CharField(max_length=100, required=False)
    category_id = serializers.IntegerField(write_only=True, required=False)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, min_value=0)
    quantity = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)