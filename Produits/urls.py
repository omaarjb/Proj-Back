# urls.py
from django.urls import path
from .views import produit_list, produit_detail

urlpatterns = [
    path('produits/', produit_list, name='produit-list'),
    path('produits/<int:pk>/', produit_detail, name='produit-detail'),
]
