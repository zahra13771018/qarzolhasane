from rest_framework import serializers
from .models import LoanRequest, Trans, Profile, Message

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'

class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trans
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
