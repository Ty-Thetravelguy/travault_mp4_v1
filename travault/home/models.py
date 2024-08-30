from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, blank=True)
    line3 = models.CharField(max_length=100, blank=True)
    line4 = models.CharField(max_length=100, blank=True)
    line5 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.line1}, {self.line2}, {self.line3}, {self.line4}, {self.line5}"

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
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

class CompanyUser(models.Model):
    USER_ROLES = (
        ('user', 'User'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')

    def __str__(self):
        return f"{self.user.username} - {self.company.company_name} - {self.get_role_display()}"

    def is_admin(self):
        return self.role == 'admin'

    def is_manager(self):
        return self.role == 'manager'

    def is_user(self):
        return self.role == 'user'

    def can_add_supplier(self):
        return self.role in ['manager', 'admin']

    def can_manage_users(self):
        return self.role == 'admin'