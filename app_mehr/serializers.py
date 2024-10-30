from rest_framework import serializers
from .models import LoanRequest, Profile, Message, Trans

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['id', 'loan_type', 'request_type', 'loan_amount', 'deposit_amount', 
                  'status', 'due_date']
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'first_name',
            'phone_number',
            'national_id',
            'profile_picture', 
            'national_id_picture',
            'guarantor_search'
        ]
        read_only_fields = ['id', 'user']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'title', 'description', 'ticket_priority', 'created_at']  # تغییر priority به ticket_priority
        read_only_fields = ['id', 'created_at']

class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trans
        fields = ['id', 'user']
        read_only_fields = ['id', 'user']
