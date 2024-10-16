# app_mehr/forms.py
from django import forms
from .models import LoanRequest

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ['loan_type', 'request_type', 'loan_amount', 'deposit_amount', 'status', 'due_date', 'installment_number', 'total_deposit_amount', 'rank']
