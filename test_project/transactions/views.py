from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from rest_framework import permissions


# Create your views here.

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
