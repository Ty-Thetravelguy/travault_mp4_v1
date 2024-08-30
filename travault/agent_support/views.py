# views.py
from django.shortcuts import render, redirect, get_object_or_404
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
    suppliers = AgentSupportSupplier.objects.filter(company=company_user.company).order_by('supplier_name')
    supplier_types = AgentSupportSupplier.SUPPLIER_TYPES
    
    return render(request, 'agent_support/index.html', {
        'suppliers': suppliers,
        'supplier_types': supplier_types,  # Add this line to pass supplier types
    })

@login_required
@role_required(['manager', 'admin'])
def add_agent_support_supplier(request):
    try:
        company_user = request.user.companyuser
        print(f"Adding supplier for: {company_user.company}")
    except CompanyUser.DoesNotExist:
        messages.error(request, "Company user association is missing. Contact your administrator.")
        return redirect('home')  # Or a relevant page
    
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


@login_required
@role_required(['manager', 'admin'])  # Restrict access to Managers and Admins
def edit_supplier(request, id):
    supplier = get_object_or_404(AgentSupportSupplier, id=id)  # Fetch supplier by ID

    if request.method == 'POST':
        form = AgentSupportSupplierForm(request.POST, instance=supplier)  # Bind form with existing supplier instance
        if form.is_valid():
            form.save()  # Save the updated supplier
            messages.success(request, 'Supplier updated successfully!')
            return redirect('agent_support:agent_support_home')  # Redirect to the home page
        else:
            messages.error(request, 'Please correct the errors below.')  # Handle form errors
    else:
        form = AgentSupportSupplierForm(instance=supplier)  # Pre-fill the form with the supplier's current details

    return render(request, 'agent_support/edit_supplier.html', {'form': form, 'supplier': supplier})  # Render edit page


@login_required
@role_required(['manager', 'admin'])  # Restrict access to Managers and Admins
def delete_supplier(request, id):
    supplier = get_object_or_404(AgentSupportSupplier, id=id)  # Fetch supplier by ID

    if request.method == 'POST':
        # Get the name entered by the user from the form
        confirmation_name = request.POST.get('confirmation_name')

        if confirmation_name == supplier.supplier_name:  # Check if entered name matches supplier name
            supplier.delete()  # Delete the supplier
            messages.success(request, 'Supplier deleted successfully!')
            return redirect('agent_support:agent_support_home')  # Redirect to the home page
        else:
            messages.error(request, 'The supplier name you entered does not match. Please try again.')

    # Render a confirmation page if GET or if the name does not match
    return render(request, 'agent_support/delete_supplier.html', {'supplier': supplier})