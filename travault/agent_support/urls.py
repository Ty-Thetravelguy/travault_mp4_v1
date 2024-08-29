from django.urls import path
from . import views

app_name = 'agent_support'

urlpatterns = [
    path('', views.agent_support_home, name='agent_support_home'),
    # path('search/', views.search_support_items, name='search_support_items'),
]