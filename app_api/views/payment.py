from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Payments
from ..serializers import PaymentSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_payment(request):
    if request.method == 'GET':
        payment = Payments.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_payment_by_id(request, id):
    if request.method == 'GET':
        try:
            payment = Payments.objects.get(pk=id)
        except:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    if request.method == 'POST':
        new_payment = request.data
        serializer = PaymentSerializer(data=new_payment)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)

class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    