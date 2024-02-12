from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Loans
from ..serializers import LoanSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_loans(request):
    if request.method == 'GET':
        loans = Loans.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_loans(request):
    if request.method == 'POST':
        new_loan = request.data
        serializer = LoanSerializer(data=new_loan)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_loans_by_id(request, id):
    if request.method == 'GET':
        try:
            loan = Loans.objects.get(pk=id)
        except:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = LoanSerializer(loan)
        
        return Response(serializer.data)
