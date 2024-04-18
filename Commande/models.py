from django.db import models
from Clients.models import Client


# Create your models here.
class Commande(models.Model):
    id_comm = models.AutoField(primary_key=True)
    date_comm = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_comm
