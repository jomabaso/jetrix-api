from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tablero
from .serializers import TableroSerializador, RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


class TableroListCreate(generics.ListCreateAPIView):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializador


class TableroCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializador
    
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
