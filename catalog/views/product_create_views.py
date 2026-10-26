from ..models import Product 
from ..serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser,FormParser

class ProductCreateView(GenericAPIView):
    serializer_class=ProductSerializer
    parser_classes=[MultiPartParser , FormParser]  
    permission_classes=[IsAdminUser]
      
    @extend_schema(request={"multipart/form-data": ProductSerializer}, responses= ProductSerializer)
    def post(self , request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)