from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Sale, SaleItem
from inventory.models import StockItem
import json
from django.utils import timezone

# Create your views here.
@csrf_exempt
@login_required
def complete_sale(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_items = data.get('cartItems', [])
            total = data.get('total', 0)

            if not cart_items:
                return JsonResponse({'error': 'Cart is empty'}, status=400)

            sale = Sale.objects.create(total=total, cashier=request.user)

            for item in cart_items:
                product_id = item.get('id')  
                quantity = item.get('quantity')
                price = item.get('price')

                try:
                    product = StockItem.objects.get(id=product_id)
                    if product.quantity < quantity:
                        return JsonResponse({'error': f"Not enough stock for {product.product_name}"}, status=400)

                    product.quantity -= quantity
                    product.save()

                    SaleItem.objects.create(
                        sale=sale,
                        product=product,
                        quantity=quantity,
                        price=price
                    )

                except StockItem.DoesNotExist:
                    return JsonResponse({'error': 'Product not found'}, status=404)

            return JsonResponse({'message': 'Sale completed successfully', 'sale_id': sale.id})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def sale_receipt(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale_items = sale.items.select_related('product')  # thanks to related_name='items'

    context = {
        'sale': sale,
        'items': sale_items,          # keep the key name consistent with the template
        'cashier': sale.cashier,      # <- use cashier, not user
        'date': sale.date,            # <- your model field is `date`, not `created_at`
    }
    return render(request, 'sales/receipt.html', context)

from django.db.models import Sum, F
from django.shortcuts import render
from .models import Sale

@login_required
def sales_report(request):
    query = request.GET.get('q', '')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    sales = Sale.objects.all().order_by('-sold_on')

    if start_date and end_date:
        sales = sales.filter(sold_on__date__range=[start_date, end_date])
    
    if query:
        sales = sales.filter(product__product_name__icontains=query)

    total_revenue = sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    total_items = sales.aggregate(Sum('quantity_sold'))['quantity_sold__sum'] or 0

    return render(request, 'sales/sales_report.html', {
        'sales': sales,
        'total_revenue': total_revenue,
        'total_items': total_items,
        'query': query,
        'start_date': start_date,
        'end_date': end_date,
    })
