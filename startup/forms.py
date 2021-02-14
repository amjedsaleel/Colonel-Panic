# Django
from django import forms

# local Django
from . models import Company, BankAccount


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'subtitle', 'description', 'location', 'employees', 'theme', 'revenue', 'expected_revenue']

