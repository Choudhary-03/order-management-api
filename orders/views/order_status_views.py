from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema

from ..models.order import Order
from ..serializers import  OrderStatusSerializer

class OrderStatusView(GenericAPIView):
    queryset= Order.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAdminUser]
    
    def patch(self, request, pk):
        order = get_object_or_404(self.get_queryset(), pk = pk)
        serializer= self. get_serializer(order, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
             