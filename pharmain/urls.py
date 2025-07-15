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
from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', account_views.logoutUser, name="logout"),
    path('register/', account_views.register, name='register'),
    path('dashboard/', account_views.dashboard, name='dashboard'),
    path('users/', account_views.users_list, name='users'),
    path('new-user/', account_views.addUser, name='new-user'),
    path('users/<int:user_id>/edit/', account_views.editUser, name='edit-user'),
    path('users/<int:user_id>/delete/', account_views.deleteUser, name='delete-user'),
    path('my-profile/edit/', account_views.edit_my_profile, name='update-profile'),
   
]
