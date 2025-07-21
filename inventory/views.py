from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from .models import StockItem
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect


@login_required
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

@login_required
def show_stock(request):
    stockitems = StockItem.objects.all()
    return render(request, 'inventory/all_stock.html', {'stockitems': stockitems})

@user_passes_test(lambda u: u.is_staff)
def edit_stock(request, stockitem_id):
    stockitem_obj = get_object_or_404(StockItem, pk=stockitem_id)
    form = StockForm(request.POST or None, instance=stockitem_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Changes successfully saved')
        return redirect('all-stock') 
    return render(request, 'inventory/edit_stock.html', {'form': form, 'stockitem_obj': stockitem_obj})

@user_passes_test(lambda u: u.is_staff)
def delete_stock(request, stockitem_id):
    stockitem_obj = get_object_or_404(StockItem, pk=stockitem_id)
    if request.method == "POST":
        stockitem_obj.delete()
        return redirect('all-stock') 
    return render(request, 'inventory/confirm_delete_stock.html', {'stockitem_obj': stockitem_obj})
