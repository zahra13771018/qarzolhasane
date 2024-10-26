from rest_framework import generics
from .models import LoanRequest
from .models import Profile
from .models import Message
from .models import Trans
from .serializers import ProfileSerializer
from .serializers import MessageSerializer
from .serializers import TransSerializer
from .serializers import LoanRequestSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def loan_request_list(request):
#     if request.user.is_authenticated:
#         all_loan_requests = request.user.loan_requests.all()
#         serializer = LoanRequestSerializer(all_loan_requests, many=True)
#         return Response(serializer.data)
#     return Response({'message': 'no loan'})

class LoanRequestListCreateView(generics.ListCreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    # فقط کاربران احراز هویت شده می‌توانند به این endpoint دسترسی داشته باشند
    permission_classes = [IsAuthenticated]

# class LoanRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LoanRequest.objects.all()
#     serializer_class = LoanRequestSerializer



# class TransListCreateView(generics.ListCreateAPIView):
#     queryset = Trans.objects.all()
#     serializer_class = TransSerializer

# class TransDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Trans.objects.all()
#     serializer_class = TransSerializer

# class ProfileListCreateView(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


# class MessageListCreateView(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer





