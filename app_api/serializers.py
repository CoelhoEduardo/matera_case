from rest_framework import serializers

from .models import Loans, Payments

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
