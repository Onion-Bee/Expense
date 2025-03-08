from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense


from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)  # Show only user’s expenses
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


from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('expense_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('expense_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

