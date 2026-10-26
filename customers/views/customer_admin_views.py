from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from customers.serializers import CustomerSerializer
from customers.models import Customer
from customers.permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

class CustomerAdminDetailView(GenericAPIView):
    queryset=Customer.objects.all()
    serializer_class= CustomerSerializer
    permission_classes=[IsAuthenticated, IsSuperUser]
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk= self.kwargs['pk'])
    
    def get(self, request, pk):
        customers= self.get_object()
        serializer=self.get_serializer(customers)
        return Response(serializer.data)
    
    @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    def put(self , request, pk):
        customer = self.get_object()
        serializer= self.get_serializer(customer, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    def patch(self,request, pk):
        customer=self.get_object()
        serializer= self.get_serializer(customer, data=request.data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        customer= self.get_object()
        customer.delete()
        return Response(status= 204)