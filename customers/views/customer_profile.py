from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from customers.serializers import CustomerSerializer
from customers.models import Customer
from customers.permissions import IsProfileOwner
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

class CustomerProfileView(GenericAPIView):
    serializer_class = CustomerSerializer
    permission_classes=[IsAuthenticated, IsProfileOwner]
    
    def get_object(self):
        customer=get_object_or_404(Customer, user=self.request.user)
        self.check_object_permissions(self.request, customer)
        return customer
    
    def get(self, request):
        customer = self.get_object()
        serializer= self.get_serializer(customer)
        return Response(serializer.data)

    @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    def put(self , request):
        customer = self.get_object()
        serializer= self.get_serializer(customer, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    def patch(self,request):
        customer=self.get_object()
        serializer= self.get_serializer(customer, data=request.data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        customer= self.get_object()
        customer.delete()
        return Response(status= 204)
        

                    
    
    # @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    # def post(self,request):
    #     customers=Customer.objects.all()
    #     serializer=CustomerSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=201)
    #     return Response (serializer.errors,status=400)
    