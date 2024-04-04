
from django.urls import path
from .views import commande_list, commande_detail

urlpatterns = [
    path('commandes/', commande_list, name='commande-list'),
    path('commandes/<int:pk>/', commande_detail, name='commande-detail'),
]
