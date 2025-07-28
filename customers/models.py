from django.db import models
from django.conf import settings
# Create your models here.
    
class Customer(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200, blank=True)
    medical_notes = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

