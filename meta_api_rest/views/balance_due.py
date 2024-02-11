from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Loans, Payments
from ..serializers import LoanSerializer, PaymentSerializer

@api_view(['GET'])
def get_balance_due(request, id):
    if request.method == 'GET':
        try:
            loan = Loans.objects.get(pk=id)
            payment = Payments.objects.all().filter(loan_id=id)
        except:
            return Response(status.HTTP_404_NOT_FOUND)
        loan_serializer = LoanSerializer(loan)
        pay_serializer = PaymentSerializer(payment, many=True)

        def map_balance(loan, payment):
            balance = dict()
            balance['customer'] = loan['customer']
            balance['loan_value'] = loan['nominal_value']
            balance['interest_rate'] = loan['interest_rate']
            calc_perc = balance['loan_value'] * balance['interest_rate']
            balance['balance_due'] = (calc_perc + balance['loan_value'])
            total_payed = 0
            for i in range(len(payment)):
                total_payed += payment[i]['payment_value']
            balance['total_payed'] = total_payed
            balance['to_pay'] = balance['balance_due'] - total_payed
            balance['payments'] = payment
            
            return balance
        
    return Response(map_balance(loan_serializer.data,pay_serializer.data))
    