from django.contrib import admin
from .models import StockItem, Supplier, Category

admin.site.register(StockItem)
admin.site.register(Supplier)
admin.site.register(Category)
