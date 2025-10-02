from django.contrib.auth.models import User
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Pack
from .serializers import (
    PackSerializer, 
    MyTokenObtainPairSerializer, 
    RegisterSerializer
)

# --- Pack Views ---

class PackListView(generics.ListCreateAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['serial_number', 'part_number']

class PackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'serial_number'

# --- Authentication Views ---

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer