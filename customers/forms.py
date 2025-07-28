from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'medical_notes',
        ]
        widgets = {
            'medical_notes': forms.Textarea(attrs={'rows': 3}),
        }
