from ..models import Product
from ..serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ProductListView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='category',
                type=str,
                enum=['cloth', 'Electronics', 'stationary', 'Footwear',
                      'Home & Kitchen', 'Personal Care', 'Sports & Fitness',
                      'Grocery', 'Computer Accessories'],
                description='Select a category',
            ),
        ],
        responses=ProductSerializer(many=True),
    )
    def get(self, request):
        queryset = self.get_queryset()                         # fixed: no ()

        category = request.query_params.get('category')        # read the param
        if category:
            queryset = queryset.filter(category__name__iexact=category)  # filter the queryset

        serializer = self.get_serializer(queryset, many=True)  # pass data, many=True
        return Response(serializer.data)