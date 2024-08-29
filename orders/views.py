from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order, User  # Importing models to use in views
from django.urls import reverse
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


# View to display all orders for a specific clinic
def order_list(request, clinic_id):
    clinic = get_object_or_404(User, pk=clinic_id)  # Fetch the clinic based on ID
    orders = Order.objects.filter(clinic=clinic)  # Get all orders related to this clinic
    return render(request, 'orders/order_list.html', {'clinic': clinic, 'orders': orders})

# View to handle the creation of a new order
@login_required
def create_order(request, clinic_id):
    clinic = get_object_or_404(User, pk=clinic_id)  # Fetch the clinic based on ID
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.clinic = clinic
            new_order.save()
            return redirect(reverse('orders:order_list', args=[clinic_id]))  # Redirect to the order list
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form, 'clinic': clinic})

def edit_order(request, clinic_id, order_id):
    # Fetch the clinic based on its ID from the User model
    clinic = get_object_or_404(User, id=clinic_id, role='clinic')  # Assuming 'role' field differentiates clinics
    order = get_object_or_404(Order, id=order_id, user=clinic)  # Fetch the order associated with the clinic
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # Redirect back to the order list view after editing
            return redirect('orders:order_list', clinic_id=clinic.id)
    else:
        form = OrderForm(instance=order)
    
    # Render the edit order page with the form and order details
    return render(request, 'orders/edit_order.html', {'form': form, 'order': order, 'clinic': clinic})