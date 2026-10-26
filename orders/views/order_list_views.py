from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from ..models.order import Order
from ..serializers.order_serializers import OrderSerializer

class OrderListView(GenericAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
    
    def get(self,request):
        serializer=self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
            
    def post(self, request):
        serializer= self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save(customer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
             