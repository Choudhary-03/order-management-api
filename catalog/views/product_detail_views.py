from ..models import Product 
from ..serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser,FormParser

class ProductDetailView(GenericAPIView):
    serializer_class=ProductSerializer
    parser_classes=[MultiPartParser , FormParser]
    permission_classes=[IsAdminUser]
    
    def get_queryset(self):
        return Product.objects.all()
        

    @extend_schema(request=ProductSerializer, responses= ProductSerializer)
    def put(self, request, pk):
        product = get_object_or_404(self.get_queryset(), pk=pk)
        serializer= self.get_serializer(product, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        product = get_object_or_404(self. get_queryset() , pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                