from django.contrib import admin

# Register your models here.
from .models import Loans, Payments

admin.site.register(Loans)
admin.site.register(Payments)
