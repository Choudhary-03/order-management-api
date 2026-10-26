from ..models import Product 
from ..serializers.product_patch_serializers import ProductPatchSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser,FormParser

class ProductRetrieveView(GenericAPIView):
    serializer_class=ProductPatchSerializer
    parser_classes=[MultiPartParser , FormParser]
    permission_classes=[IsAdminUser]
    
    def get_queryset(self):
        return Product.objects.all()
        
    @extend_schema(request=ProductPatchSerializer(partial=True), responses= ProductPatchSerializer)
    def patch(self, request, pk):
        product = get_object_or_404(self.get_queryset(), pk=pk)
        serializer= self.get_serializer(product, data = request.data, partial=True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status= 200)