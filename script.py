###################### THIS SCRIPT IS ALREADY EXECUTED, DO NOT ATTEMPT TO RUN IT AGAIN #################################
######################                       B9IT M3AHA 3H                             #################################

import os
import requests
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bi3Smart.settings")
django.setup()

from Categorie.models import Categorie
from Produits.models import Produit


def populate_categories():
    url = "https://fakestoreapi.com/products/categories"
    response = requests.get(url)
    if response.status_code == 200:
        categories = response.json()
        i = 0
        for category in categories:
            i += 1
            Categorie.objects.create(
                id_category=i,
                nom_categorie=category
            )
        print("Populated categories successfully")


def populate_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            category = Categorie.objects.filter(nom_categorie=product['category']).first()
            Produit.objects.create(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                image=product['image'],
                category=category,
                description=product['description']

            )
        print("all products populated")


populate_products()
