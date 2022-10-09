from django.contrib.auth.models import User
from rest_framework import serializers
from wallets.models import Wallet


class UserSerializer(serializers.ModelSerializer):
    wallets = serializers.PrimaryKeyRelatedField(many=True, queryset=Wallet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'wallets']
