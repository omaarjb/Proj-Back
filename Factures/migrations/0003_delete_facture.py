# Generated by Django 5.0.3 on 2024-04-19 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Factures', '0002_remove_facture_client'),
        ('Ligne_Commandes', '0002_alter_ligne_commande_unique_together_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Facture',
        ),
    ]