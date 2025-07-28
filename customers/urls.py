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
from customers import views as views




urlpatterns = [
    path('customers/', views.all_customers, name='customers'),
    path('add-customer/', views.add_customer, name='add-customer'),
    path('edit-customer/<int:customer_id>/edit/', views.edit_customer, name='edit-customer'),
    path('delete-customer/<int:customer_id>/edit/', views.delete_customer, name='delete-customer'),
   
]