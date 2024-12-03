from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, permissions, status
from .models import Tablero, Task
from .serializers import TableroSerializador, RegisterSerializer, TaskSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response


# class TableroListCreate(generics.ListCreateAPIView):
#     queryset = Tablero.objects.all()
#     serializer_class = TableroSerializador


# class TableroCRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tablero.objects.all()
#     serializer_class = TableroSerializador
    
    
# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_queryset(self):
#         return Task.objects.filter(usuario=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(usuario=self.request.user)
    
    

class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializador
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tablero.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
        
    @action(detail=True, methods=['get','post'], permission_classes=[permissions.IsAuthenticated])
    def tasks(self, request, pk=None):
        tablero = self.get_object()
        
        if request.method == 'GET':
            tareas = Task.objects.filter(tablero=tablero)
            serializer = TaskSerializer(tareas, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(tablero=tablero, usuario=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
