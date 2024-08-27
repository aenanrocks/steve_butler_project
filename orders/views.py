from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Order, User
from .forms import OrderForm


# View for listing all orders for a specific clinic
def order_list(request, clinic_id):
    clinic = get_object_or_404(User, id=clinic_id, role='clinic')
  # Get the clinic or return a 404 error
    orders = Order.objects.filter(clinic=clinic)
  # Get all orders associated with this clinic
    return render(request, 'orders/order_list.html', {'clinic': clinic, 'orders': orders})
  # Render the order list


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})

# View for creating a new order
def create_order(request, clinic_id):
    clinic = get_object_or_404(User, id=clinic_id, role='clinic')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.clinic = clinic
            order.save()
            return redirect('order_list', clinic_id=clinic.id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form, 'clinic': clinic})

# View for updating an existing order
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form, 'clinic': order.clinic, 'order': order})

def lab_dashboard(request):
    orders = Order.objects.all()
    return render(request, 'orders/lab_dashboard.html', {'orders': orders})

# View for deleting an order
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # Get the order or return a 404 error
    if request.method == 'POST':
        order.delete()  # Delete the order from the database
        return redirect('order_list', clinic_id=order.clinic.id)  # Redirect to the order list view
    return render(request, 'orders/delete_order.html', {'order': order})  # Render a confirmation page before deletion
