# urls.py
from django.urls import path
from .views import categorie_list, categorie_detail

urlpatterns = [
    path('categories/', categorie_list, name='categorie-list'),
    path('categories/<int:pk>/', categorie_detail, name='categorie-detail'),
]
