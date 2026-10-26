from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation

User= get_user_model()
class RegisterSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True, min_length=8, trim_whitespace= False)
    
    def validate_username(self,value):
        value=value.strip()
        
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('this username already exists')
        return value
    
    def validate_email(self, value):
        value=value.strip() 
        
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('this email already exists')
        return value
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
