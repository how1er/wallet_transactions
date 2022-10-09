from .models import Wallet
from .serializers import WalletSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class WalletList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WalletDetail(generics.RetrieveDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
