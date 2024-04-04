
from rest_framework import serializers
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['Id_produit', 'nom_prod', 'prix', 'categorie']
