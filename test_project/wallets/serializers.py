from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wallet
        fields = ['id', 'name', 'owner', 'type', 'currency', 'balance', 'created_on', 'modified_on']

    def create(self, validated_data):
        owner = validated_data.get('owner')
        if owner.wallets.count() == 5:
            raise serializers.ValidationError({"wallets": "user has enough wallets"})

        return Wallet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.balance = validated_data.get('balance', instance.balance)
        instance.balance = validated_data.get('type', instance.balance)
        instance.balance = validated_data.get('currency', instance.balance)
        instance.save()
        return instance

        # validated_data.pop("type", None)
        # validated_data.pop("currency", None)
        # return super().update(instance, validated_data)
