from rest_framework import serializers
from .models import Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nom', 'prenom', 'password', 'email', 'adresse']

    def validate_email(self, value):
        if 'email' in self.initial_data:
            email = self.initial_data['email']
            if email == value:
                return value
            if Client.objects.filter(email=value).exists():
                raise serializers.ValidationError("Email address already exists.")
        return value
