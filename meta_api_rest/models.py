from django.db import models
from uuid import uuid4
import random
import socket
import struct

# Create your models here.
class Loans(models.Model):
    creat_ip_address = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nominal_value = models.FloatField()
    interest_rate = models.FloatField()
    ip_adress = models.GenericIPAddressField(default=creat_ip_address)
    created_at = models.DateField(auto_now_add=True)
    bank = models.CharField(max_length=10)
    customer = models.CharField(max_length=30)

    def __str__(self):
        return f'id: {str(self.id)} | customer: {self.customer}'

class Payments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    loan_id = models.ForeignKey(Loans, on_delete=models.CASCADE)
    payment_value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'id: {str(self.id)} | loan_id: {str(self.loan_id)} | payment: {self.payment_value}'
