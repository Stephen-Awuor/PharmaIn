from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StockForm
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # or 'add-stock', etc.
    return redirect('login')

@login_required
def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock item added successfully!")
            return redirect('add-stock')  # or wherever you want
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StockForm()
    
    return render(request, 'inventory/add_stock.html', {'form': form})
