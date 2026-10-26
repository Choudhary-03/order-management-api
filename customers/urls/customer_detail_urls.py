from django.urls import path
from customers.views import CustomerAdminDetailView

urlpatterns=[
    path('superuser/<int:pk>',CustomerAdminDetailView.as_view(), name='admin_detail_view'),

]