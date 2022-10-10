from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from rest_framework import permissions
from wallets.models import Wallet

from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TransactionDetail(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       ]
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     return user.wallets.all()


class TransactionWallet(generics.RetrieveAPIView):
    lookup_field = ''
    serializer_class = TransactionSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       ]
    #
    def get_queryset(self):
        queryset = Transaction.objects.filter(Q(sender=self.lookup_field) | Q(receiver=self.lookup_field))
        return queryset


@api_view(['GET'])
def transactions_of_wallet(request, name):
    transactions = Transaction.objects.filter(Q(sender=name) | Q(receiver=name))
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
