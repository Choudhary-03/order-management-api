from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from customers.serializers import CustomerSerializer
from customers.models import Customer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema


class CustomerCreateView(GenericAPIView):
    serializer_class=CustomerSerializer
    permission_classes=[IsAuthenticated]
    
    def post(self, request):
        
        if Customer.objects.filter(user=request.user).exists():
            return Response(status=400)
            
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
