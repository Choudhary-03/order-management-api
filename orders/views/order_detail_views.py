from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import  IsAuthenticated
from drf_spectacular.utils import extend_schema

from ..models.order import Order
from ..serializers.order_serializers import OrderSerializer
    
class OrderDetailView(GenericAPIView):
    serializer_class= OrderSerializer
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
    
    def get(self, request, pk):
        order= get_object_or_404(self.get_queryset(),pk=pk)
        serializer= self.get_serializer(order)
        return Response(serializer.data)

             