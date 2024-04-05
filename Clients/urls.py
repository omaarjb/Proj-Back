from django.urls import path
from .views import clients_list, clients_detail
urlpatterns = [
    path('clients/', clients_list, name='client-list'),
    path('clients/<int:pk>/', clients_detail, name='client-details')
]