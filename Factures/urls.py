from django.urls import path
from .views import list_facture_par_client, retrieve_facture
urlpatterns = [
    path('facture/<int:pk_client>', list_facture_par_client, name='facture-list'),
    path('clients/<int:pk>/', retrieve_facture, name='facture-details')
]