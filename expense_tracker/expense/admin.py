# from django.contrib import admin

# # Register your models here.


# from .models import Expense

# admin.site.register(Expense)
from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'transaction_type', 'category', 'date')
    list_filter = ('transaction_type', 'category', 'date')
    search_fields = ('title', 'category')
