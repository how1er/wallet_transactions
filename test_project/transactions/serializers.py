from rest_framework import serializers, status
from .models import Transaction
from wallets.models import Wallet
from rest_framework.response import Response


class TransactionSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Transaction
        fields = ['creator', 'sender', 'receiver', 'transfer_amount', 'commission', 'status', 'timestamp']

    def validate_sender(self, name):
        try:
            wallet = Wallet.objects.get(name=name)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError("sender does not exists")
        return wallet

    def validate_receiver(self, name):
        try:
            wallet = Wallet.objects.get(name=name)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError("receiver does not exists")
        return wallet

    def commission(self, sender, receiver):
        if sender.owner == receiver.owner:
            return 0
        else:
            return 10

    def transfer(self, sender, receiver, amount, commission):
        total_amount = amount + (amount * commission / 100)
        if sender.balance < total_amount:
            raise serializers.ValidationError("sender doesnt have enough balance")
        sender.balance = sender.balance - total_amount
        receiver.balance = receiver.balance + amount
        sender.save()
        receiver.save()
        return True

    def create(self, validated_data):

        validated_data['commission'] = self.commission(validated_data['sender'], validated_data['receiver'])
        if self.transfer(validated_data['sender'], validated_data['receiver'],
                         validated_data['transfer_amount'], validated_data['commission']):
            status_of_tr = 'paid'
        else:
            status_of_tr = 'fail'

        validated_data['status'] = status_of_tr
        return Transaction.objects.create(**validated_data)

    def save(self, **kwargs):
        self.validated_data['sender'] = self.validate_sender(self.validated_data['sender'])
        self.validated_data['receiver'] = self.validate_sender(self.validated_data['receiver'])
        if self.validated_data['sender'].currency != self.validated_data['receiver'].currency:
            raise serializers.ValidationError("currencies does not match")
        super().save(**kwargs)

