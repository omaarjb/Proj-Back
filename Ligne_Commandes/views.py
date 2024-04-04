from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ligne_Commande
from .serializers import LigneCommandeSerializer

@api_view(['GET', 'POST'])
def ligne_commande_list(request):
    if request.method == 'GET':
        lignes_commande = Ligne_Commande.objects.all()
        serializer = LigneCommandeSerializer(lignes_commande, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LigneCommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ligne_commande_detail(request, pk):
    try:
        ligne_commande = Ligne_Commande.objects.get(pk=pk)
    except Ligne_Commande.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LigneCommandeSerializer(ligne_commande)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LigneCommandeSerializer(ligne_commande, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ligne_commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
