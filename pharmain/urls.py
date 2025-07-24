"""
URL configuration for pharmain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', account_views.logoutUser, name="logout"),
    path('register/', account_views.register, name='register'),

    # User management
    path('dashboard/', account_views.dashboard, name='dashboard'),
    path('users/', account_views.users_list, name='users'),
    path('new-user/', account_views.addUser, name='new-user'),
    path('users/<int:user_id>/edit/', account_views.editUser, name='edit-user'),
    path('users/<int:user_id>/delete/', account_views.deleteUser, name='delete-user'),
    path('my-profile/edit/', account_views.edit_my_profile, name='update-profile'),
   
    # Password reset routes
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # Inventory routes (use root path for clean URLs)
    path('', include('inventory.urls')),
    path('sales/', include('sales.urls')),
]

