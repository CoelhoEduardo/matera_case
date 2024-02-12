from django.test import TestCase
from django.urls import reverse

from .models import Loans, Payments

class LoansTestCase(TestCase):
    def setUpLoan(self):

        return Loans.objects.create(nominal_value=2000.00, interest_rate=0.05, bank=b'Itau', customer=b'Edu')
    
    def test_loan_creation(self):
        loan = self.setUpLoan()
        self.assertTrue(isinstance(loan, Loans))
        to_test = f'id: {str(loan.id)} | customer: {loan.customer}'
        self.assertEqual(loan.__str__(), to_test)
    
    def test_loan_list_view(self):
        loan = self.setUpLoan()
        url = reverse("get_loan_by_id", args=[str(loan.id)])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(loan.customer, resp.content)

class PaymentTestCase(TestCase):
    def setUpLoan(self):
        return Loans.objects.create(nominal_value=2000.00, interest_rate=0.05, bank=b'Itau', customer=b'Edu')
    
    def setUp(self):
        loan = self.setUpLoan()
        return Payments.objects.create(loan_id=loan, payment_value=300.00)
    
    def test_payment_creation(self):
        payment = self.setUp()
        self.assertTrue(isinstance(payment, Payments))
        to_test = f'id: {str(payment.id)} | loan_id: {str(payment.loan_id)} | payment: {payment.payment_value}'
        self.assertEqual(payment.__str__(), to_test)
    
class BalanceTestCase(TestCase):
     def setUpLoan(self):
        return Loans.objects.create(nominal_value=2000.00, interest_rate=0.05, bank=b'Itau', customer=b'Edu')
    
     def setUpPayment(self):
        loan = self.setUpLoan()
        return Payments.objects.create(loan_id=loan, payment_value=300.00)
     
     def test_balance_due(self):
         loan = self.setUpLoan()
         url = reverse('get_balance_due', args=[str(loan.id)])
         resp = self.client.get(url)

         self.assertIn(loan.customer, resp.content)
