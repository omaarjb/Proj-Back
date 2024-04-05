from .models import Facture
from rest_framework import serializers

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = ["num_facture", "client", "montant"]
