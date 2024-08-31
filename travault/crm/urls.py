from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.index, name='crm_home'),
] # Add this line to your urls.py file in the crm app. This will make the root URL of the crm app point to the index view.
