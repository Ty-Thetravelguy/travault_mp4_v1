from django.contrib import admin
from django.urls import path, include
from home.views import logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('logout/', logout_view, name='logout'),    
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('agent_support/', include('agent_support.urls')),
    path('users/', include('users.urls')),  # Add this line
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('crm/', include('crm.urls')),  
]
