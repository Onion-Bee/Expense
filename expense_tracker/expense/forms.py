from django import forms
# from .models import Expense
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Expense Form
# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = ['title', 'amount', 'category']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
#             'category': forms.Select(attrs={'class': 'form-select'}),
#         }
from .models import Transaction
from .models import Transaction, CATEGORY_CHOICES, TRANSACTION_TYPES
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'transaction_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = CATEGORY_CHOICES
        self.fields['transaction_type'].choices = TRANSACTION_TYPES


# Sign-Up Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # Set placeholder text

# Login Form
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
