from django.contrib import admin
from django.urls import path, include
from home.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('logout/', logout_view, name='logout'),    
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]
