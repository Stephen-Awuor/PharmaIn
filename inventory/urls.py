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
from inventory import views as views
from inventory import views as inventory_views
from sales import views as sales_views
from .views import export_stock_to_excel
from .views import export_supplier_to_excel
from .views import export_category_to_excel


urlpatterns = [
    path('', views.index, name='index'),  # handles root '/'
    path('add-stock/', views.add_stock, name='add-stock'),
    path('all-stock/', views.show_stock, name='all-stock'),
    path('stockitem/<int:stockitem_id>/edit/', views.edit_stock, name='edit-stock'),
    path('stockitem/<int:stockitem_id>/delete/', views.delete_stock, name='delete-stock'),
    path('pos/', views.pos_view, name='pos'),
    path('pos/search/', views.pos_search, name='pos_search'),
    path('suppliers/', views.all_suppliers, name='suppliers'),
    path('add-new-supplier/', views.add_supplier, name='add-new-supplier'),
    path('edit-supplier-info/<int:supplier_id>/edit/', views.edit_supplier, name='edit-supplier-info'),
    path('delete-supplier/<int:supplier_id>/edit/', views.delete_supplier, name='delete-supplier'),
    path('categories/', views.stock_categories, name='categories'),
    path('add-new-category/', views.add_category, name='add-new-category'),
    path('edit-category-info/<int:category_id>/edit/', views.edit_category, name='edit-category-info'),
    path('delete-category/<int:category_id>/edit/', views.delete_category, name='delete-category'),
    path('export-stock/', export_stock_to_excel, name='export-stock'),
    path('export-supplier/', export_supplier_to_excel, name='export-supplier'),
    path('export-category/', export_category_to_excel, name='export-category'),

    # other inventory routes...
]