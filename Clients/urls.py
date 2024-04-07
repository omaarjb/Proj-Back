from django.urls import path
from .views import clients_list, clients_detail
urlpatterns = [
    path('clients/register/', clients_list, name='client-list'),
    path('clients/register/<int:pk>/', clients_detail, name='client-details')
]