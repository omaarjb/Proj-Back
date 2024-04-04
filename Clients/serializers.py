from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id_client', 'nom', 'prenom', 'email', 'adresse']