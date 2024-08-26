from django.urls import path
from . import views

urlpatterns = [
    path('clinic/<int:clinic_id>/orders/', views.order_list, name='order_list'),  # URL for listing orders
    path('clinic/<int:clinic_id>/orders/create/', views.create_order, name='create_order'),  # URL for creating an order
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),  # URL for updating an order
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),  # URL for deleting an order
]
