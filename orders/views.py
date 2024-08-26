from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Order, User

# View for listing all orders for a specific clinic
def order_list(request, clinic_id):
    clinic = get_object_or_404(User, id=clinic_id, role='CLINIC')  # Get the clinic or return a 404 error
    orders = Order.objects.filter(clinic=clinic)  # Get all orders associated with this clinic
    return render(request, 'orders/order_list.html', {'clinic': clinic, 'orders': orders})  # Render the order list

# View for creating a new order
def create_order(request, clinic_id):
    clinic = get_object_or_404(User, id=clinic_id, role='CLINIC')  # Get the clinic or return a 404 error
    if request.method == 'POST':
        details = request.POST.get('details')
        finish_date = request.POST.get('finish_date')
        delivery_method = request.POST.get('delivery_method')
        # Create and save the order
        order = Order.objects.create(clinic=clinic, details=details, finish_date=finish_date, delivery_method=delivery_method)
        return redirect('order_list', clinic_id=clinic.id)  # Redirect to the order list view after creating the order
    return render(request, 'orders/create_order.html', {'clinic': clinic})  # Render the order creation form

# View for updating an existing order
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # Get the order or return a 404 error
    if request.method == 'POST':
        order.details = request.POST.get('details')
        order.status = request.POST.get('status')
        order.notes = request.POST.get('notes')
        order.delivery_method = request.POST.get('delivery_method')
        order.save()  # Save the updated order to the database
        return redirect('order_list', clinic_id=order.clinic.id)  # Redirect to the order list view
    return render(request, 'orders/update_order.html', {'order': order})  # Render the order update form

# View for deleting an order
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # Get the order or return a 404 error
    if request.method == 'POST':
        order.delete()  # Delete the order from the database
        return redirect('order_list', clinic_id=order.clinic.id)  # Redirect to the order list view
    return render(request, 'orders/delete_order.html', {'order': order})  # Render a confirmation page before deletion
