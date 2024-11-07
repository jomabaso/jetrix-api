from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tablero
from .serializers import TableroSerializador

class TableroListCreate(generics.ListCreateAPIView):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializador


class TableroCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializador