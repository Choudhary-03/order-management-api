from django.urls import path
from ..views import OrderListView, OrderDetailView, OrderStatusView

urlpatterns = [
    path('order/', OrderListView.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view()),
    path('order/status/<int:pk>', OrderStatusView.as_view())
]