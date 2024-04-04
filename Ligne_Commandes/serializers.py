
from rest_framework import serializers
from .models import Ligne_Commande

class LigneCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne_Commande
        fields = '__all__'
