from django.db import models
from django.conf import settings
from inventory.models import StockItem


class Sale(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sold_on = models.DateTimeField(auto_now_add=True)
    cashier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Sale #{self.id} - {self.date.strftime('%Y-%m-%d %H:%M')}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(StockItem, on_delete=models.PROTECT)
    quantity_sold = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total(self):
        return self.quantity_sold * self.product.selling_price

    def __str__(self):
        return f"{self.quantity_sold} x {self.product.product_name} (KES {self.total_amount})"
