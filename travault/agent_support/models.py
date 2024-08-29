from django.db import models
from django.conf import settings

class AgentSupportSupplier(models.Model):
    SUPPLIER_TYPES = [
        ('air', 'Air'),
        ('accommodation', 'Accommodation'),
        ('ground_transportation', 'Ground Transportation'),
        ('rail', 'Rail'), 
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    supplier_type = models.CharField(max_length=50, choices=SUPPLIER_TYPES)
    supplier_name = models.CharField(max_length=100)
    agent_websites = models.TextField(blank=True, null=True)
    contact_numbers = models.TextField(blank=True, null=True)
    group_email = models.TextField(blank=True, null=True)
    general_email = models.TextField(blank=True, null=True)
    account_manager = models.CharField(max_length=100, blank=True, null=True)
    account_manager_contact = models.CharField(max_length=100, blank=True, null=True)
    account_manager_email = models.EmailField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.supplier_name} - {self.get_supplier_type_display()}"