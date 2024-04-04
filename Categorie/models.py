from django.db import models

# Create your models here.
class Categorie(models.Model):
    Id_categorie = models.AutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_categorie

