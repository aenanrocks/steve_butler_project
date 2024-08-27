from django.urls import path
from . import views

app_name = 'orders'  # Namespace for this app's URLs

urlpatterns = [
    path('clinic/<int:clinic_id>/orders/', views.order_list, name='order_list'),
    path('clinic/<int:clinic_id>/orders/create/', views.create_order, name='create_order'),
]
