from django.urls import path
from ..views import ProductListView,ProductDetailView, ProductCreateView,ProductRetrieveView
urlpatterns=[
    path('product/', ProductListView.as_view(), name='get_product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/create/<int:pk>', ProductRetrieveView.as_view(), name='patch_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]