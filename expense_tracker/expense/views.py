from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction


from django.contrib.auth.decorators import login_required
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    net_balance = total_income - total_expense
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_balance': net_balance,
    }
    return render(request, 'transaction_list.html', context)

from .forms import TransactionForm  # Create this form in the next step

@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})



from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('transaction_list')
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
            messages.success(request, "✅ Successfully logged in!")
            return redirect('transaction_list')  # Redirect to dashboard
        else:
            messages.error(request, "❌ Invalid username or password!")  # Error message for incorrect credentials

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


from django.contrib.auth import logout

def logout_view(request):
    if request.method == "POST" or request.method == "GET":  
        logout(request)
        return render(request, 'logout.html')
    return redirect('transaction_list')  

def landing_page(request):
    return render(request, 'landing.html')


# @login_required
# def view_graph(request):
#     transactions = Transaction.objects.filter(user=request.user)
    
#     total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
#     total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')

#     context = {
#         'total_income': total_income,
#         'total_expense': total_expense,
#     }
#     return render(request, 'graph.html', context)

from collections import defaultdict
import json

@login_required
def view_graph(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("date")

    income_data = defaultdict(float)
    expense_data = defaultdict(float)

    for t in transactions:
        date = t.date.strftime("%Y-%m-%d")  # Convert to string for JSON compatibility
        amount = float(t.amount)  # Convert Decimal to float
        if t.transaction_type == "income":
            income_data[date] += amount
        else:
            expense_data[date] += amount

    dates = sorted(set(income_data.keys()) | set(expense_data.keys()))
    income_values = [income_data[date] for date in dates]
    expense_values = [expense_data[date] for date in dates]

    context = {
        "dates": json.dumps(dates),
        "income_values": json.dumps(income_values),
        "expense_values": json.dumps(expense_values),
    }
    return render(request, "graph.html", context)
