from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AgentSupportSupplierForm
from .models import AgentSupportSupplier


class AddAgentSupportSupplierViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('agent_support:add_agent_support_supplier')


def test_add_agent_support_supplier_valid_form(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': 'air',
        'supplier_name': 'Test Supplier',
        'agent_websites': 'www.test.com',
        'contact_numbers': '1234567890',
        'group_email': 'test@test.com',
        'general_email': 'info@test.com',
        'account_manager': 'Test Manager',
        'account_manager_contact': '0987654321',
        'account_manager_email': 'manager@test.com',
        'other': 'Additional information'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('agent_support:agent_support_home'))
    self.assertEqual(AgentSupportSupplier.objects.count(), 1)
    self.assertEqual(AgentSupportSupplier.objects.first().supplier_name, 'Test Supplier')
    self.assertEqual(AgentSupportSupplier.objects.first().user, self.user)
    self.assertEqual(str(list(messages.get_messages(response.wsgi_request))[0].message), 'Supplier added successfully!')


def test_add_agent_support_supplier_invalid_form(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': 'invalid_type',
        'supplier_name': '',
        'account_manager_email': 'invalid_email'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'There was an error in the form. Please check and try again.')
    self.assertEqual(AgentSupportSupplier.objects.count(), 0)

def test_add_agent_support_supplier_redirect_to_home(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': 'air',
        'supplier_name': 'Test Supplier',
        'agent_websites': 'www.test.com',
        'contact_numbers': '1234567890',
        'group_email': 'test@test.com',
        'general_email': 'info@test.com',
        'account_manager': 'Test Manager',
        'account_manager_contact': '0987654321',
        'account_manager_email': 'manager@test.com',
        'other': 'Additional information'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('agent_support:agent_support_home'))

def test_add_agent_support_supplier_invalid_form(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': 'invalid_type',
        'supplier_name': '',
        'account_manager_email': 'invalid_email'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'There was an error in the form. Please check and try again.')
    self.assertEqual(AgentSupportSupplier.objects.count(), 0)

def test_add_agent_support_supplier_unauthenticated(self):
    data = {
        'supplier_type': 'air',
        'supplier_name': 'Test Supplier',
        'agent_websites': 'www.test.com',
        'contact_numbers': '1234567890',
        'group_email': 'test@test.com',
        'general_email': 'info@test.com',
        'account_manager': 'Test Manager',
        'account_manager_contact': '0987654321',
        'account_manager_email': 'manager@test.com',
        'other': 'Additional information'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/accounts/login/?next=' + self.url)
    self.assertEqual(AgentSupportSupplier.objects.count(), 0)

def test_add_agent_support_supplier_case_sensitivity(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': 'AiR',  # Uppercase 'AiR' instead of 'air'
        'supplier_name': 'Test Supplier',
        'agent_websites': 'www.test.com',
        'contact_numbers': '1234567890',
        'group_email': 'test@test.com',
        'general_email': 'info@test.com',
        'account_manager': 'Test Manager',
        'account_manager_contact': '0987654321',
        'account_manager_email': 'manager@test.com',
        'other': 'Additional information'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('agent_support:agent_support_home'))
    self.assertEqual(AgentSupportSupplier.objects.count(), 1)
    self.assertEqual(AgentSupportSupplier.objects.first().supplier_type, 'air')  # Check if the supplier_type is converted to lowercase

def test_add_agent_support_supplier_required_fields(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': '',  # Required field
        'supplier_name': '',  # Required field
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'This field is required.')
    self.assertEqual(AgentSupportSupplier.objects.count(), 0)

def test_add_agent_support_supplier_unique_fields(self):
    self.client.login(username='testuser', password='testpassword')
    # Create a supplier with unique fields
    AgentSupportSupplier.objects.create(
        user=self.user,
        supplier_type='air',
        supplier_name='Unique Supplier',
        vat_number='123456789',
        company_reg_number='987654321'
    )
    # Try to create another supplier with the same unique fields
    data = {
        'supplier_type': 'air',
        'supplier_name': 'Unique Supplier',
        'vat_number': '123456789',
        'company_reg_number': '987654321'
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'A company with this name already exists.')
    self.assertContains(response, 'A company with this VAT number already exists.')
    self.assertContains(response, 'A company with this registration number already exists.')
    self.assertEqual(AgentSupportSupplier.objects.count(), 1)

def test_add_agent_support_supplier_missing_fields(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': '',  # Missing required field
        'supplier_name': '',  # Missing required field
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'This field is required.')
    self.assertEqual(AgentSupportSupplier.objects.count(), 0)

def test_add_agent_support_supplier_extra_fields(self):
    self.client.login(username='testuser', password='testpassword')
    data = {
        'supplier_type': 'air',
        'supplier_name': 'Test Supplier',
        'agent_websites': 'www.test.com',
        'contact_numbers': '1234567890',
        'group_email': 'test@test.com',
        'general_email': 'info@test.com',
        'account_manager': 'Test Manager',
        'account_manager_contact': '0987654321',
        'account_manager_email': 'manager@test.com',
        'other': 'Additional information',
        'extra_field': 'Extra data'  # Adding an extra field
    }
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('agent_support:agent_support_home'))
    self.assertEqual(AgentSupportSupplier.objects.count(), 1)
    self.assertEqual(AgentSupportSupplier.objects.first().supplier_name, 'Test Supplier')
    self.assertEqual(AgentSupportSupplier.objects.first().user, self.user)
    self.assertEqual(messages.get_messages(response.wsgi_request)._loaded_messages[0].message, 'Supplier added successfully!')