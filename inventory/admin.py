from django.contrib import admin
from .models import StockItem, Supplier, Category, Sale, SaleItem

admin.site.register(StockItem)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(SaleItem)