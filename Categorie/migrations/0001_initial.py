# Generated by Django 5.0.3 on 2024-04-02 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('Id_categorie', models.AutoField(primary_key=True, serialize=False)),
                ('nom_categorie', models.CharField(max_length=200)),
            ],
        ),
    ]
