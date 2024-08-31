from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, blank=True)
    line3 = models.CharField(max_length=100, blank=True)
    line4 = models.CharField(max_length=100, blank=True)
    line5 = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'agency'
    
    def __str__(self):
        return f"{self.line1}, {self.line2}, {self.line3}, {self.line4}, {self.line5}"

class AgencyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agency_profile')
    company_name = models.CharField(max_length=100, unique=True)
    vat_number = models.CharField(max_length=15, unique=True)
    company_reg_number = models.CharField(max_length=15, unique=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    employees = models.CharField(max_length=20)
    business_focus = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name

