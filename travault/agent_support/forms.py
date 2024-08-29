from django import forms
from .models import AgentSupportSupplier

class AgentSupportSupplierForm(forms.ModelForm):
    agent_websites = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        help_text="Enter multiple websites separated by commas if you have more than one.",
        required=False
    )
    contact_numbers = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        help_text="Enter multiple numbers separated by commas if you have more than one.",
        required=False
    )
    group_email = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        help_text="Enter multiple emails separated by commas if you have more than one.",
        required=False
    )
    general_email = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        help_text="Enter multiple emails separated by commas if you have more than one.",
        required=False
    )
    other = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = AgentSupportSupplier
        fields = ['supplier_type', 'supplier_name', 'agent_websites', 'contact_numbers', 
                  'group_email', 'general_email', 'account_manager', 'account_manager_contact', 
                  'account_manager_email', 'other']
        widgets = {
            'supplier_type': forms.Select(attrs={'class': 'form-control'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'account_manager_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'account_manager_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['supplier_type', 'supplier_name']:
                self.fields[field].required = False