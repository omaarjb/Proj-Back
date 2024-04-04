from django.db import models
from Commande.models import Commande
from Produits.models import Produit
from Factures.models import Facture

class Ligne_Commande(models.Model):
    id_comm = models.ForeignKey(Commande, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    num_facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    Quantite = models.IntegerField()

    class Meta:
       
        unique_together = (('id_comm', 'id_prod', 'num_facture'),)
