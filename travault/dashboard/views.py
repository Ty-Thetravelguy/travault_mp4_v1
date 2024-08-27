from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html') 
