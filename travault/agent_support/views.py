from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AgentSupportSupplierForm
from .models import AgentSupportSupplier
from home.models import CompanyUser
from .decorators import role_required

@login_required
@role_required(['user', 'manager', 'admin'])
def agent_support_home(request):
    company_user = request.user.companyuser
    suppliers = AgentSupportSupplier.objects.filter(company=company_user.company)
    return render(request, 'agent_support/index.html', {'suppliers': suppliers})

@login_required
@role_required(['manager', 'admin'])
def add_agent_support_supplier(request):
    company_user = request.user.companyuser

    if request.method == 'POST':
        form = AgentSupportSupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user
            supplier.company = company_user.company
            supplier.save()
            messages.success(request, 'Supplier added successfully!')
            return redirect('agent_support:agent_support_home')
        else:
            messages.error(request, 'There was an error in the form. Please check and try again.')
    else:
        form = AgentSupportSupplierForm()
    return render(request, 'agent_support/add_supplier.html', {'form': form})