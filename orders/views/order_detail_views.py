from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import  IsAuthenticated,IsAdminUser
from drf_spectacular.utils import extend_schema

from ..models.order import Order
from ..serializers.order_serializers import OrderSerializer
    
class OrderDetailView(GenericAPIView):
    serializer_class= OrderSerializer
    permission_classes= [IsAuthenticated, IsAdminUser]
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

             