from django.db import models

# Create your models here.
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
    