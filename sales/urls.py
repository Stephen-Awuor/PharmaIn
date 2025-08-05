# sales/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('complete-sale/', views.complete_sale, name='pos_finish'),
    path('receipt/<int:sale_id>/', views.sale_receipt, name='sale-receipt'),
    path('sales-report/', views.sales_report, name='sales-report'),
    path('export-sales-report/', views.export_report_to_excel, name='export-sales-report'),

    

]
