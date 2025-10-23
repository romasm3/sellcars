from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
import uuid

from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserProfileForm,
    UserPasswordChangeForm,
    ForgotPasswordForm,
    PasswordResetForm
)
from .models import User


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome!')
            return redirect('accounts:profile')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_short_name()}!')
                next_url = request.GET.get('next', 'accounts:profile')
                return redirect(next_url)
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    """User logout view"""
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
    return redirect('accounts:login')


@login_required
def profile(request):
    """User profile view"""
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def profile_edit(request):
    """Edit user profile view"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {'form': form})


@login_required
def password_change(request):
    """Change password view"""
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('accounts:profile')
    else:
        form = UserPasswordChangeForm(request.user)

    return render(request, 'accounts/password_change.html', {'form': form})


def forgot_password(request):
    """Forgot password view - sends reset email"""
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)

            # Generate password reset token
            user.password_reset_token = uuid.uuid4()
            user.password_reset_token_created = timezone.now()
            user.save()

            # Build reset URL
            reset_url = request.build_absolute_uri(
                reverse('accounts:password_reset', kwargs={'token': user.password_reset_token})
            )

            # Send email
            subject = 'Password Reset Request - SellCars'
            message = f'''
Hello {user.get_short_name()},

You requested a password reset for your SellCars account.

Click the link below to reset your password:
{reset_url}

This link will expire in 24 hours.

If you didn't request this, please ignore this email.

Best regards,
SellCars Team
'''
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            messages.success(
                request,
                'Password reset instructions have been sent to your email.'
            )
            return redirect('accounts:login')
    else:
        form = ForgotPasswordForm()

    return render(request, 'accounts/forgot_password.html', {'form': form})


def password_reset(request, token):
    """Password reset view - resets password with token"""
    try:
        user = User.objects.get(password_reset_token=token)
    except User.DoesNotExist:
        messages.error(request, 'Invalid password reset link.')
        return redirect('accounts:login')

    if not user.is_password_reset_token_valid():
        messages.error(request, 'Password reset link has expired. Please request a new one.')
        return redirect('accounts:forgot_password')

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.password_reset_token = None
            user.password_reset_token_created = None
            user.save()

            messages.success(request, 'Password reset successfully! You can now log in.')
            return redirect('accounts:login')
    else:
        form = PasswordResetForm()

    return render(request, 'accounts/password_reset.html', {
        'form': form,
        'token': token
    })
