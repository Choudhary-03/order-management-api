"""
URL configuration for order_managementApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView,)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Account/', include('accounts.urls.auth_urls')),
    path('category/api/', include('catalog.urls.category_urls')),
    path('product/api/', include('catalog.urls.product_urls')),

    path('order/api/', include('orders.urls.order_urls')),
    path('Create_customer/api/', include('customers.urls.create_customer_urls')),
    path('customer_detail/api/', include('customers.urls.customer_detail_urls')),
    path('customer_profile/api/', include('customers.urls.customer_profile_urls')),



# jwt    
    path(
    'api/token/',
    TokenObtainPairView.as_view(),
    name='token_obtain_pair'
),
path(
    'api/token/refresh/',
    TokenRefreshView.as_view(),
    name='token_refresh'
),

    # API schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
