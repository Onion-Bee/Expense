from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

from .forms import ExpenseForm  # Create this form in the next step

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def update_expense(request, id):
    expense = get_object_or_404(Expense, id=id)  # Fetch existing expense
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)  # Update existing record
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect back to main list
    else:
        form = ExpenseForm(instance=expense)  # Pre-fill form with existing data
    return render(request, 'update_expense.html', {'form': form})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == "POST":
        expense.delete()
        return redirect('expense_list')
    return render(request, 'delete_expense.html', {'expense': expense})
