from django.db import models

# User model for clinics and labs
class User(models.Model):
    name = models.CharField(max_length=100)  # Name of the clinic or lab
    email = models.EmailField(unique=True)   # Unique email address
    ROLE_CHOICES = [
        ('CLINIC', 'Clinic'),
        ('LAB', 'Lab'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Role selection

    def __str__(self):
        return f"{self.name} ({self.role})"  # String representation of the model

# Order model for managing dental lab orders
class Order(models.Model):
    clinic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')  # Link to the clinic
    details = models.TextField()  # Order details
    notes = models.TextField(blank=True, null=True)  # Optional notes
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')  # Status of the order
    finish_date = models.DateField()  # Date by which the order should be completed
    DELIVERY_METHOD_CHOICES = [
        ('PICKUP', 'Pickup'),
        ('POST', 'Post'),
        ('EMAIL', 'Email'),
    ]
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_METHOD_CHOICES)  # Delivery method
    notification_status = models.BooleanField(default=False)  # Notification status

    def __str__(self):
        return f"Order {self.id} for {self.clinic.name} - Status: {self.status}"  # String representation
