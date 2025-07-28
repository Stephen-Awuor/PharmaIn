from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm
from .models import Customer

# Create your views here.
@login_required
def all_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/current_customers.html', {'customers': customers})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully!")
            return redirect('customers')  # or wherever you want
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomerForm()
    
    return render(request, 'customers/add_customer.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def edit_customer(request, customer_id):
    customer_obj = get_object_or_404(Customer, pk=customer_id)
    form = CustomerForm(request.POST or None, instance=customer_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Changes successfully saved')
        return redirect('customers') 
    return render(request, 'customers/edit_customer.html', {'form': form, 'customer_obj': customer_obj})

@user_passes_test(lambda u: u.is_staff)
def delete_customer(request, customer_id):
    customer_obj = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        customer_obj.delete()
        return redirect('customers') 
    return render(request, 'customers/confirm_delete_customer.html', {'customer_obj': customer_obj})