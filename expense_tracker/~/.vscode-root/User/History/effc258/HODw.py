from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Shopping', 'Shopping'),
    ('Bills', 'Bills'),
    ('Other', 'Other'),
]

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null values
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount} ({self.user.username if self.user else 'No User'})"
