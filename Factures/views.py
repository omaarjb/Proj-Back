from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Facture
from .serializers import FactureSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def list_facture_(request, pk_client):
    if request.method == 'GET':
        factures = Facture.objects.filter(client=pk_client)
        serializer = FactureSerializer(factures, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_facture(request, pk):
    try:
        facture = Facture.objects.get(pk=pk)
    except Facture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FactureSerializer(facture)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = FactureSerializer(facture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        facture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)