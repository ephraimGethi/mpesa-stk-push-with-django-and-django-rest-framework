from rest_framework import serializers

class MpesaPaymentSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    amount = serializers.IntegerField()
    account_reference = serializers.CharField(max_length=50)
    transaction_desc = serializers.CharField(max_length=100)
