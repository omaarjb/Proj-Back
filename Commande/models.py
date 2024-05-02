from django.db import models
from Clients.models import Client


# Create your models here.
class Commande(models.Model):
    id_comm = models.AutoField(primary_key=True)
    date_comm = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=0)
    montant_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id_comm)
