# Generated by Django 5.0.3 on 2024-04-19 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Commande', '0002_alter_commande_date_comm'),
        ('Ligne_Commandes', '0001_initial'),
        ('Produits', '0002_rename_categorie_produit_category_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ligne_commande',
            unique_together={('id_comm', 'id_prod')},
        ),
        migrations.RemoveField(
            model_name='ligne_commande',
            name='num_facture',
        ),
    ]
