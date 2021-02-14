# Django
from django.contrib import admin

# local django
from . models import Company, BankAccount

# Register your models here.

admin.site.register(Company)
admin.site.register(BankAccount)
