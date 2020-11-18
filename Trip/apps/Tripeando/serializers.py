from rest_framework import serializers
from apps.Tripeando.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usuario','nombre','apellido','email']