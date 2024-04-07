from django.db import models
from Categorie.models import Categorie

# Create your models here.
class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description= models.CharField(max_length=255,default=' ')
    image = models.CharField(max_length=255,default=' ')
    def __str__(self):
        return self.nom_prod
