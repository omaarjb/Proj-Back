# urls.py
from django.urls import path
from .views import ligne_commande_list, ligne_commande_detail

urlpatterns = [
    path('ligne_commandes/', ligne_commande_list, name='ligne-commande-list'),
    path('ligne_commandes/<int:pk>/', ligne_commande_detail, name='ligne-commande-detail'),
]
