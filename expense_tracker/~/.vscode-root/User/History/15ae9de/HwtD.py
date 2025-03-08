from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})
