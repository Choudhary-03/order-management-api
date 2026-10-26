from django.urls import path
from ..views.auth_views import RegisterCreateView, RegisterDetailView

urlpatterns=[
    path('register/',RegisterCreateView.as_view(), name='register'),
    path('register/detail/',RegisterDetailView.as_view(), name='register')

]