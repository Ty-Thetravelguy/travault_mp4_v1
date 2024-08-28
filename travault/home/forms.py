from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CompanyProfile, Address, CompanyUser

class CustomUserCreationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100, required=True)
    company_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        required=True,
        help_text="Enter your address, with each line separated by a newline character."
    )
    vat_number = forms.CharField(max_length=15, required=True, label="VAT Number")  # Added field for VAT number
    company_reg_number = forms.CharField(max_length=15, required=True, label="Company Registration Number")  # Added field for company reg number
    phone_number = forms.CharField(max_length=20, required=True)
    contact_full_name = forms.CharField(max_length=100, required=True, label="Primary Contact Full Name",
                                        help_text="Enter the full name (first and last name) of the primary contact.")
    email = forms.EmailField(required=True)
    employees = forms.ChoiceField(choices=[
        ('', 'Select range'),
        ('1-10', '1-10'),
        ('11-50', '11-50'),
        ('51-100', '51-100'),
        ('100+', '100+')
    ], required=True)
    business_focus = forms.ChoiceField(choices=[
        ('', 'Select focus'),
        ('corporate', 'Corporate Travel'),
        ('leisure', 'Leisure Travel'),
        ('mixed', 'Mixed')
    ], required=True)
    agree_terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'company_name', 'company_address', 'vat_number', 'company_reg_number', 'phone_number', 
                  'contact_full_name', 'email', 'employees', 'business_focus', 
                  'agree_terms', 'password1', 'password2')

    def clean_company_name(self):
        company_name = self.cleaned_data.get('company_name')
        if CompanyProfile.objects.filter(company_name=company_name).exists():
            raise forms.ValidationError("A company with this name already exists.")
        return company_name

    def clean_vat_number(self):
        vat_number = self.cleaned_data.get('vat_number')
        if CompanyProfile.objects.filter(vat_number=vat_number).exists():
            raise forms.ValidationError("A company with this VAT number already exists.")
        return vat_number

    def clean_company_reg_number(self):
        reg_number = self.cleaned_data.get('company_reg_number')
        if CompanyProfile.objects.filter(company_reg_number=reg_number).exists():
            raise forms.ValidationError("A company with this registration number already exists.")
        return reg_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        full_name = self.cleaned_data.get('contact_full_name', '')
        name_parts = full_name.split(None, 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        user.first_name = first_name
        user.last_name = last_name
        
        if commit:
            user.save()

            # Create Address instance
            address_lines = self.cleaned_data['company_address'].split('\n')
            address = Address.objects.create(
                line1=address_lines[0],
                line2=address_lines[1] if len(address_lines) > 1 else '',
                line3=address_lines[2] if len(address_lines) > 2 else '',
                line4=address_lines[3] if len(address_lines) > 3 else '',
                line5=address_lines[4] if len(address_lines) > 4 else ''
            )

            # Create CompanyProfile instance
            company_profile = CompanyProfile.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                vat_number=self.cleaned_data['vat_number'],
                company_reg_number=self.cleaned_data['company_reg_number'],
                address=address,
                phone_number=self.cleaned_data['phone_number'],
                contact_first_name=first_name,
                contact_last_name=last_name,
                employees=self.cleaned_data['employees'],
                business_focus=self.cleaned_data['business_focus']
            )

            # Create CompanyUser instance, setting the user as the admin
            CompanyUser.objects.create(
                user=user,
                company=company_profile,
                is_company_admin=True
            )

        return user