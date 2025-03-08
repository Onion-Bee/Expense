# from django.urls import path
# from .views import (
#     landing_page, 
#     transaction_list, add_transaction,
#     signup_view, login_view, logout_view
# )

# urlpatterns = [
#     path('', landing_page, name='landing_page'),
#     path('dashboard/', transaction_list, name='transaction_list'),
#     path('transaction/add/', add_transaction, name='add_transaction'),
#     path('signup/', signup_view, name='signup'),
#     path('login/', login_view, name='login_user'),
#     path('logout/', logout_view, name='logout_user'),
# ]
from django.urls import path
from .views import (
    landing_page, 
    transaction_list, add_transaction, view_graph,
    signup_view, login_view, logout_view
)

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('dashboard/', transaction_list, name='transaction_list'),
    path('transaction/add/', add_transaction, name='add_transaction'),
    path('graph/', view_graph, name='view_graph'),  # New Graph URL
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login_user'),
    path('logout/', logout_view, name='logout_user'),
]
