from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from ..serializers import RegisterSerializer
from ..models import Accounts
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema

class RegisterDetailView(GenericAPIView):
    serializer_class=RegisterSerializer
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        serializer=RegisterSerializer(request.user)
        return Response(serializer.data)

class RegisterCreateView(GenericAPIView):
    serializer_class= RegisterSerializer
    permission_classes=[AllowAny]
    authentication_classes=[]    
    
    @extend_schema(request=RegisterSerializer, responses=RegisterSerializer)
    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            
            data={ 'id':account.id,
                  'name':account.username,
                  'email':account.email}
        
            return Response(data, status=201)
        return Response(serializer.errors, status=400)

