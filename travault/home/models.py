from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, blank=True)
    line3 = models.CharField(max_length=100, blank=True)
    line4 = models.CharField(max_length=100, blank=True)
    line5 = models.CharField(max_length=100, blank=True)

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=100, unique=True)
    vat_number = models.CharField(max_length=15, unique=True)  # Ensure VAT number is unique
    company_reg_number = models.CharField(max_length=15, unique=True)  # Ensure Company Reg Number is unique
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    employees = models.CharField(max_length=20)
    business_focus = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name

class CompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    is_company_admin = models.BooleanField(default=False)  # Indicates if the user is an admin of the company

    def __str__(self):
        return f"{self.user.username} - {self.company.company_name}"
