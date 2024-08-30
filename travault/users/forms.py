from django import forms
from django.contrib.auth.models import User
from home.models import CompanyUser

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop('company', None)
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.company:
            query = CompanyUser.objects.filter(company=self.company, user__username=username)
            if self.instance:
                query = query.exclude(user=self.instance)
            if query.exists():
                raise forms.ValidationError("A user with this username already exists in your company.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.company:
            query = CompanyUser.objects.filter(company=self.company, user__email=email)
            if self.instance:
                query = query.exclude(user=self.instance)
            if query.exists():
                raise forms.ValidationError("A user with this email already exists in your company.")
        return email

class CompanyUserForm(forms.ModelForm):
    class Meta:
        model = CompanyUser
        fields = ['role']