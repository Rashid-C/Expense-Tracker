from django.urls import path
from .views import ExpenseListCreateView


urlpatterns = [
    path('expenses/', ExpenseListCreateView(),name='expense-list-create')
]
