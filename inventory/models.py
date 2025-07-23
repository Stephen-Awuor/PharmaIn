from django.db import models
from django.conf import settings
# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class StockItem(models.Model):
    product_name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cashier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Sale #{self.id} - {self.date.strftime('%Y-%m-%d %H:%M')}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(StockItem, on_delete=models.PROTECT)  # 🔄 changed here
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} (KES {self.price})"