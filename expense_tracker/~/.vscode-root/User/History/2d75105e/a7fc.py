from django.urls import path
from .views import (
    expense_list, add_expense, update_expense, delete_expense, 
    signup_view, login_view, logout_view
)

urlpatterns = [
    # Expense management URLs
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('update/<int:id>/', update_expense, name='update_expense'),
    path('delete/<int:id>/', delete_expense, name='delete_expense'),

    # Authentication URLs
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'
         ),
]
