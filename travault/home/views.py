from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    """ A view to return the index page. """
    return render (request, 'home/index.html')

def terms_of_service(request):
    """ A view to return the Terms of Service page. """
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    """ A view to return the Privacy Policy page. """
    return render(request, 'privacy_policy.html')

# def register(request):
#     print("Register view called")
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, f"Welcome to TraVault, {user.username}!")
#             return redirect('dashboard') 
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})