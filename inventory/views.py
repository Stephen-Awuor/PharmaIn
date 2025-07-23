from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StockForm
from django.contrib.auth.decorators import login_required
from .models import StockItem, Sale, SaleItem
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model
User = get_user_model()


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


@csrf_exempt
def pos_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        items = StockItem.objects.filter(product_name__icontains=query)
        for item in items:
            results.append({
                'id': item.id,
                'product_name': item.product_name,
                'selling_price': str(item.selling_price)
            })
    return JsonResponse({'results': results})

def pos_view(request):
    products = StockItem.objects.all()
    return render(request, 'your_pos_template.html', {'products': products})

@csrf_exempt
@login_required
def complete_sale(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_items = data.get('cartItems', [])
        total = data.get('total', 0)

        if not cart_items:
            return JsonResponse({'error': 'Cart is empty'}, status=400)

        sale = Sale.objects.create(
            total=total,
            cashier=request.user
        )

        for item in cart_items:
            product_id = item.get('productId')
            quantity = item.get('quantity')
            price = item.get('price')

            try:
                product = StockItem.objects.get(id=product_id)
                if product.quantity < quantity:
                    return JsonResponse({'error': f"Not enough stock for {product.product_name}"}, status=400)

                # Deduct stock
                product.quantity -= quantity
                product.save()

                # Save the sale item
                SaleItem.objects.create(
                    sale=sale,
                    product=product,
                    quantity=quantity,
                    price=price
                )

            except StockItem.DoesNotExist:
                return JsonResponse({'error': 'Product not found'}, status=404)

        return JsonResponse({'message': 'Sale completed successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)