#api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tablero


class TableroSerializador(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = ['id','titulo_tablero','description','fecha_publicacion']
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','username','password','email']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data.get('first_name',''),
            username = validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password']
        )
        return user