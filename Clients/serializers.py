from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id_client', 'nom', 'prenom','password', 'email', 'adresse']

    def validate_email(self, value):
        if Client.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address already exists .")
        return value
    













  
