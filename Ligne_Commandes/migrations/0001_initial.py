# Generated by Django 5.0.3 on 2024-04-04 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Commande', '0001_initial'),
        ('Factures', '0001_initial'),
        ('Produits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ligne_Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantite', models.IntegerField()),
                ('id_comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Commande.commande')),
                ('id_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produit')),
                ('num_facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Factures.facture')),
            ],
            options={
                'unique_together': {('id_comm', 'id_prod', 'num_facture')},
            },
        ),
    ]
