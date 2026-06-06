from rest_framework import serializers
from .models import Expense
from django.utils import timezone


class ExpenseSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Expense
        fields=['id','title','amount','date','category','created_at','user']
        
    def validate_amount(self,value):
        if value <=0:
            raise serializers.ValidationError('The amount must be a positive number')
        return value
    
    def validate(self,data):
        if data['date']>timezone.now():
            raise serializers.ValidationError({"date":"You can't log an expense in future."})
        return data