from ..models.product_models import Category 
from rest_framework.permissions import IsAdminUser
from ..serializers.category_serializers import CategorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from drf_spectacular.utils import extend_schema

class CategoryListView(GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAdminUser]
    
    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    @extend_schema(request=CategorySerializer, responses= CategorySerializer)
    def post(self , request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
class CategoryDetailView(GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAdminUser]

        
    @extend_schema(request=CategorySerializer, responses= CategorySerializer)
    def put(self, request, pk):
        category = get_object_or_404(self.get_queryset(), pk=pk)
        serializer= self.get_serializer(category, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(request=CategorySerializer, responses= CategorySerializer)
    def patch(self, request, pk):
        category = get_object_or_404(self.get_queryset(), pk=pk)
        serializer= self.get_serializer(category, data = request.data, partial=True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    

    def delete(self, request, pk):
        category = get_object_or_404(self. get_queryset() , pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
