from django.urls import path
from .views import (
    landing_page, expense_list, add_expense, update_expense, delete_expense,
    signup_view, login_view, logout_view
)

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Set landing page as default
    path('dashboard/', expense_list, name='expense_list'),  # Moved expense list to "/dashboard/"
    path('add/', add_expense, name='add_expense'),
    path('update/<int:id>/', update_expense, name='update_expense'),
    path('delete/<int:id>/', delete_expense, name='delete_expense'),
    
    # Authentication URLs
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login_user'),
    path('logout/', logout_view, name='logout_user'),
]
path('login-user/', login_view, name='login_user'),
