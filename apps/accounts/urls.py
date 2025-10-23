from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Registration
    path('register/', views.register, name='register'),

    # Login/Logout
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Profile
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # Password Management
    path('password/change/', views.password_change, name='password_change'),
    path('password/forgot/', views.forgot_password, name='forgot_password'),
    path('password/reset/<uuid:token>/', views.password_reset, name='password_reset'),
]
