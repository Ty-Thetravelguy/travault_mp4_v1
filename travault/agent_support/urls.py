# agent_support/urls.py
from django.urls import path
from . import views

app_name = 'agent_support'

urlpatterns = [
    path('', views.agent_support_home, name='agent_support_home'),
    path('add-supplier/', views.add_agent_support_supplier, name='add_supplier'),
    path('edit-supplier/<int:id>/', views.edit_supplier, name='edit_supplier'),  # Edit route
    path('delete-supplier/<int:id>/', views.delete_supplier, name='delete_supplier'),  # Delete route
    
]
