from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Shopping', 'Shopping'),
    ('Bills', 'Bills'),
    ('Other', 'Other'),
]

class Expense(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"
