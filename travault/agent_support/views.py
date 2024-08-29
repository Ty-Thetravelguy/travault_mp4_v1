from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import AgentSupportSupplierForm

@login_required
def agent_support_home(request):
    return render(request, 'agent_support/index.html')

@login_required
def add_agent_support_supplier(request):
    if request.method == 'POST':
        form = AgentSupportSupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user
            supplier.save()
            messages.success(request, 'Supplier added successfully!')
            return redirect('agent_support:agent_support_home')
        else:
            messages.error(request, 'There was an error in the form. Please check and try again.')
    else:
        form = AgentSupportSupplierForm()
    return render(request, 'agent_support/add_supplier.html', {'form': form})