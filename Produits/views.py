# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

@api_view(['GET', 'POST'])
def produit_list(request):
    if request.method == 'GET':
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def produit_detail(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProduitSerializer(produit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProduitSerializer(produit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getProductId(request, title):
    try:
        produit = Produit.objects.get(title=title)
    except Produit.ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        response_data = {
            'product_id': produit.id
        }
        return Response(response_data, status=status.HTTP_200_OK)
    

        