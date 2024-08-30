from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            try:
                company_user = request.user.companyuser
                if company_user.role in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, "You don't have permission to access this page.")
                    return redirect('home')  # Redirect to home or another appropriate page
            except AttributeError:
                messages.error(request, "You are not associated with a company. Please contact your administrator.")
                return redirect('home')  # Redirect to home or another appropriate page
        return _wrapped_view
    return decorator