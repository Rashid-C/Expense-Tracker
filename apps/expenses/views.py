from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes=[permissions.IsAuthenticated] #logic of auth
    
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category','date']
    
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)       # Opti: Only show expenses belonging to the current user
    
    
    
