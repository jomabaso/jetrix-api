#api/serializers.py

from rest_framework import serializers
from .models import Tablero


class TableroSerializador(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = ['id','titulo_tablero','description','fecha_publicacion']
    