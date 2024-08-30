from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from home.models import CompanyUser
from .forms import UserForm, CompanyUserForm

@login_required
def manage_users(request):
    if not request.user.companyuser.is_admin():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('home')
    
    company_users = CompanyUser.objects.filter(company=request.user.companyuser.company)
    return render(request, 'users/manage_users.html', {'users': company_users})

@login_required
def add_user(request):
    if not request.user.companyuser.is_admin():
        messages.error(request, "You don't have permission to add users.")
        return redirect('users:manage_users')

    if request.method == 'POST':
        user_form = UserForm(request.POST, company=request.user.companyuser.company)
        company_user_form = CompanyUserForm(request.POST)
        if user_form.is_valid() and company_user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_unusable_password()
            user.save()
            company_user = company_user_form.save(commit=False)
            company_user.user = user
            company_user.company = request.user.companyuser.company
            company_user.save()

            # Generate password reset link
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )

            # Send email with password reset link
            send_mail(
                'Set Your Password',
                f'Please click the following link to set your password: {password_reset_url}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            messages.success(request, f"User {user.username} has been added successfully. An email has been sent to set their password.")
            return redirect('users:manage_users')
    else:
        user_form = UserForm(company=request.user.companyuser.company)
        company_user_form = CompanyUserForm()
    
    return render(request, 'users/add_user.html', {
        'user_form': user_form,
        'company_user_form': company_user_form
    })

@login_required
def edit_user(request, user_id):
    if not request.user.companyuser.is_admin():
        messages.error(request, "You don't have permission to edit users.")
        return redirect('users:manage_users')

    company_user = get_object_or_404(CompanyUser, id=user_id, company=request.user.companyuser.company)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=company_user.user, company=request.user.companyuser.company)
        company_user_form = CompanyUserForm(request.POST, instance=company_user)
        if user_form.is_valid() and company_user_form.is_valid():
            user_form.save()
            company_user_form.save()
            messages.success(request, f"User {company_user.user.username} has been updated.")
            return redirect('users:manage_users')
    else:
        user_form = UserForm(instance=company_user.user, company=request.user.companyuser.company)
        company_user_form = CompanyUserForm(instance=company_user)
    
    return render(request, 'users/edit_user.html', {
        'user_form': user_form,
        'company_user_form': company_user_form,
        'edit_user': company_user.user
    })

@login_required
def delete_user(request, user_id):
    if not request.user.companyuser.is_admin():
        messages.error(request, "You don't have permission to delete users.")
        return redirect('users:manage_users')

    company_user = get_object_or_404(CompanyUser, id=user_id, company=request.user.companyuser.company)
    user = company_user.user

    if request.method == 'POST':
        confirm_username = request.POST.get('confirm_username')
        if confirm_username == user.username:
            company_user.delete()
            user.delete()
            messages.success(request, f"User {user.username} has been deleted.")
            return redirect('users:manage_users')
        else:
            messages.error(request, "The username you entered doesn't match. Deletion cancelled.")

    return render(request, 'users/confirm_delete.html', {'user': user})