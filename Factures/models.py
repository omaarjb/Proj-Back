from django.db import models
from Clients.models import Client


# Create your models here.
class Facture(models.Model):
    num_facture = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
