from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import AgencyProfile, Address
from users.models import UserRoles

class AddressAdmin(admin.ModelAdmin):
    list_display = ('line1', 'line2', 'line3', 'line4', 'line5')

admin.site.register(Address, AddressAdmin)

class AgencyProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'vat_number', 'company_reg_number', 'phone_number')

admin.site.register(AgencyProfile, AgencyProfileAdmin)

class UserRolesInline(admin.StackedInline):
    model = UserRoles
    can_delete = False
    verbose_name_plural = 'Company User'

class UserAdmin(BaseUserAdmin):
    inlines = (UserRolesInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_company', 'get_role')

    def get_company(self, obj):
        return obj.userroles.company if hasattr(obj, 'userroles') else None
    get_company.short_description = 'Company'

    def get_role(self, obj):
        return obj.userroles.get_role_display() if hasattr(obj, 'userroles') else None
    get_role.short_description = 'Role'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class UserRolesAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'role')
    list_filter = ('company', 'role')
    search_fields = ('user__username', 'user__email', 'company__company_name')

admin.site.register(UserRoles, UserRolesAdmin)