from rest_framework import viewsets,permissions
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes=[permissions.IsAuthenticated] #logic of auth
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)       # Opti: Only show expenses belonging to the current user