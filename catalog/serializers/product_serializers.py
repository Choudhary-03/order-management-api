from rest_framework import serializers
from django.db import transaction
from ..models.product_models import Product
from ..models.category_models import Category

class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length = 100)
    category_id = serializers.IntegerField(write_only=True)
    unit_price=serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity=serializers.IntegerField()
    image=serializers.ImageField()
    
    created = False
    
    def validate_name(self, value):
        value= value.strip()
        if not value:
            raise serializers.ValidationError('Name cannot be blank')
        
        products=Product.objects.filter(name__iexact=value)
        if self.instance:
            products=products.exclude(pk=self.instance.pk)
            if products.exists():
                raise serializers.ValidationError('An item with this name already exists')
        return value
    
    def validate_category_id(self, value):
        if not Category.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Category does not exist")
        return value
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('quantity must be greater than 0')
        return value
    
    def validate_image(self, value):
        max_size = 2*1024*1024
        if value.size > max_size:
            raise serializers.ValidationError('image size must be 2 MB OR less')
        return value
    
    @transaction.atomic
    def create(self, validated_data):
        
        category_id = validated_data.pop('category_id')
        category= Category.objects.get(pk=category_id)
        item= Product.objects.select_for_update().filter(name__iexact=validated_data['name']).first()
        
        if item:
            if item.category_id != category.id:
                raise serializers.ValidationError(
                    "This product already exists in a different category"
                )

            if item.unit_price != validated_data['unit_price']:
                raise serializers.ValidationError(
                    "This product already exists with a different price"
                )

            item.quantity += validated_data['quantity']
            item.save(update_fields=['quantity', 'updated_at'])
            self.created = False
            return item

        self.created = True
        return Product.objects.create(category=category, **validated_data)
    

    def update(self, instance, validated_data):
        category_id = validated_data.pop("category_id", None)

        if category_id is not None:
            instance.category_id = category_id

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    
    # def update(self, instance, validated_data):
    #     instance.category_id = validated_data.get(
    #         "category_id", instance.category_id
    #     )
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.unit_price = validated_data.get(
    #         "unit_price", instance.unit_price
    #     )
    #     instance.quantity = validated_data.get(
    #         "quantity", instance.quantity
    #     )
    #     instance.image = validated_data.get("image", instance.image)

    #     instance.save()
    #     return instance
        