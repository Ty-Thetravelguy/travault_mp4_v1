from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages

def logout_view(request):
    """Logs the user out and redirects to the home page."""
    print("Custom logout view is being called!")
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home/index.html')  # Redirect to the home page or any page of your choice

def index(request):
    """ A view to return the index page. """
    return render (request, 'home/index.html')

def terms_of_service(request):
    """ A view to return the Terms of Service page. """
    return render(request, 'home/terms_of_service.html')

def privacy_policy(request):
    """ A view to return the Privacy Policy page. """
    return render(request, 'home/privacy_policy.html')

def custom_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user without logging them in
            messages.success(
                request, "You have successfully registered! Please login to proceed."
            )
            return redirect('account_login')  # Redirect to the login page after registration
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'home/register.html', {'form': form})