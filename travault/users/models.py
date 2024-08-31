from django.db import models
from django.contrib.auth.models import User
from agency.models import AgencyProfile

class UserRoles(models.Model):
    USER_ROLES = (
        ('user', 'User'),
        ('manager', 'Manager'),
        ('sales', 'Sales'),
        ('admin', 'Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(AgencyProfile, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')

    def __str__(self):
        return f"{self.user.username} - {self.company.company_name} - {self.get_role_display()}"

    def is_admin(self):
        return self.role == 'admin'

    def is_manager(self):
        return self.role == 'manager'

    def is_user(self):
        return self.role == 'user'

    def is_sales(self):
        return self.role == 'sales'

    def can_add_supplier(self):
        return self.role in ['manager', 'admin']

    def can_manage_users(self):
        return self.role == 'admin'
