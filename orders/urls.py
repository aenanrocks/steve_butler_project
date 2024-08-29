from django.urls import path
from . import views

app_name = 'orders'  # Namespace for this app's URLs

urlpatterns = [
    path('clinic/<int:clinic_id>/orders/', views.order_list, name='order_list'),  # Lists orders for a clinic
    path('clinic/<int:clinic_id>/orders/create/', views.create_order, name='create_order'),  # Creates a new order
    path('clinic/<int:clinic_id>/orders/<int:order_id>/edit/', views.edit_order, name='edit_order'),  # Edits an order


]
