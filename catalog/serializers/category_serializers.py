from rest_framework import serializers
from ..models.category_models import Category

class CategorySerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length = 100)
    description=serializers.CharField(max_length = 100)    
    
    def create(self, validated_data):  
         return Category.objects.create(**validated_data)
              