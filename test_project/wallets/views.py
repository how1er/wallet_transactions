from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Wallet
from .serializers import WalletSerializer


@api_view(['GET', 'POST'])
def wallet_list(request):
    if request.method == 'GET':
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def wallet_detail(request, name):
    try:
        wallet = Wallet.objects.get(name=name)
    except Wallet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
