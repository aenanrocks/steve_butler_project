# orders/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[('CLINIC', 'Clinic'), ('LAB', 'Lab')])

class Order(models.Model):
    clinic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    details = models.TextField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')])
    finish_date = models.DateField()
    delivery_method = models.CharField(max_length=10, choices=[('PICKUP', 'Pickup'), ('POST', 'Post'), ('EMAIL', 'Email')])
