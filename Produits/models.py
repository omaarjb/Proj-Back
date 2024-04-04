from django.db import models
from Categorie.models import Categorie

# Create your models here.
class Produit(models.Model):
    Id_produit = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_prod
