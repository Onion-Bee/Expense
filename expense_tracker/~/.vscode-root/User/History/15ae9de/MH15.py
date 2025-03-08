from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense


from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)  # Show only user’s expenses
    return render(request, 'expense_list.html', {'expenses': expenses})


from .forms import ExpenseForm  # Create this form in the next step

@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Assign expense to logged-in user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})


@login_required
def update_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)  # Ensure only owner can edit
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'update_expense.html', {'form': form})

@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)  # Ensure only owner can delete
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
            messages.success(request, "✅ Successfully logged in!")
            return redirect('expense_list')  # Redirect to dashboard
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
    return redirect('expense_list')  

def landing_page(request):
    return render(request, 'landing.html')
