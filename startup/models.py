from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()


class Company(models.Model):
    owner = models.OneToOneField(to=user, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    employees = models.PositiveIntegerField()
    theme = models.TextField(max_length=255, help_text='IT/Food/Art etc')
    revenue = models.PositiveIntegerField()
    expected_revenue = models.PositiveIntegerField()

    class Meta:
        verbose_name ='Companie'

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    owner = models.OneToOneField(to=Company, on_delete=models.CASCADE)
    account_holder = models.CharField(max_length=155, help_text='Name of the bank account owner')
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)

    def __str__(self):
        return self.account_number

