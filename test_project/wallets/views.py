from .models import Wallet
from .serializers import WalletSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class WalletList(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.wallets.all()


class WalletDetail(generics.RetrieveDestroyAPIView):
    serializer_class = WalletSerializer
    lookup_field = 'name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return user.wallets.all()


class WalletUpdate(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

