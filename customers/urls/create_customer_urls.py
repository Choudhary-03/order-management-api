from django.urls import path
from customers.views import CustomerCreateView

urlpatterns=[
    path('',CustomerCreateView.as_view(), name='create_customer'),
   
]