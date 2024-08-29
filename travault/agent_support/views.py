from django.shortcuts import render
# from django.db.models import Q
# from .models import SupportItem

def agent_support_home(request):
    return render(request, 'agent_support/index.html')
