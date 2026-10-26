import re
from rest_framework import serializers
from customers.models import Customer
class CustomerSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    first_name= serializers.CharField(max_length=100)
    last_name= serializers.CharField(max_length=100)
    phone_number=serializers.CharField(max_length=10)
    email=serializers.EmailField(max_length=100)
    address=serializers.CharField(max_length=100)
    
    def validate_first_name(self,value):
        value=value.strip()
        if not value:
            raise serializers.ValidationError('first name cannot be empty')
        return value
    
    def validate_last_name(self,value):
        value=value.strip()
        if not value:
            raise serializers.ValidationError('last name cannot be empty')
        return value
    
    def validate_address(self, value):
        value=value.strip()
        if not value:
            raise serializers.ValidationError('address cannot be empty')
        return value        
        
    def validate_phone_number(self,value):
        value= value.strip()
        
        if not re.fullmatch(r"[6-9]\d{9}", value):
            raise serializers.ValidationError("must start from 6,7,8 or 9")
        
        customers=Customer.objects.filter(phone_number= value)
        
        if self.instance:
            customers= customers.exclude(pk=self.instance.pk)
        
        if customers.exists():
            raise serializers.ValidationError('this phone number is already registered')
        return value
    
    def validate_email(self, value):
        value=value.strip().lower()
        customers= Customer.objects.filter(email__iexact=value)
        
        if self.instance:
            customers= customers.exclude(pk=self.instance.pk)
            
        if customers.exists():
            raise serializers.ValidationError('this email already exists')
        return value
    
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
    # def update(self , instance, validated_data):
        
    #     instance.first_name = validated_data['first_name']
    #     instance.last_name = validated_data['last_name']
    #     instance.phone_number = validated_data['phone_number']
    #     instance.email = validated_data['email']
    #     instance.address = validated_data['address']
        
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()
        return instance
    