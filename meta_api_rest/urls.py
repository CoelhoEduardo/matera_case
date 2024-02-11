from django.urls import path

from .views import loans, payment, balance_due

urlpatterns = [
    path('', loans.get_loans, name='get_all_loans'),
    path('loans', loans.get_loans, name='get_all_loans'),
    path('loans/create', loans.post_loans, name='post_loans'),
    path('loans/<uuid:id>', loans.get_loans_by_id, name='get_loan_by_id'),
    path('loans/<uuid:id>/balance', balance_due.get_balance_due, name='get_balance_due'),
    path('payment', payment.get_payment, name='get_payments'),
    path('payment/create', payment.create_payment, name='creat_payment'),
    path('payment/<uuid:id>', payment.get_payment_by_id, name='get_payment_by_id'),
]
