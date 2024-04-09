from django.urls import path
from .views import clients_list, clients_detail,clientsByEmail, login
urlpatterns = [
    path('clients/register/', clients_list, name='client-list'),
    path('clients/register/<int:pk>/', clients_detail, name='client-details'),
    path('clients/clientEmail/<str:email>/', clientsByEmail, name='client-by-email'),
    path('clients/login/', login, name='login'),
]