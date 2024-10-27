from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import LoanRequest
from .models import Profile
from .models import Message
from .models import Trans
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .serializers import ProfileSerializer
from .serializers import MessageSerializer
from .serializers import TransSerializer
from .serializers import LoanRequestSerializer
from rest_framework.permissions import IsAuthenticated


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [IsAuthenticated]


class LoanRequestListCreateView(generics.ListCreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    # فقط کاربران احراز هویت شده می‌توانند به این endpoint دسترسی داشته باشند
    permission_classes = [IsAuthenticated]

class LoanRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

class TransViewSet(viewsets.ModelViewSet):
    queryset = Trans.objects.all()
    serializer_class = TransSerializer
    permission_classes = [IsAuthenticated]

class TransListCreateView(generics.ListCreateAPIView):
    queryset = Trans.objects.all()
    serializer_class = TransSerializer

class TransDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trans.objects.all()
    serializer_class = TransSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    
class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class LoanRequestUpdateView(UpdateView):
    model = LoanRequest
    fields = ['loan_type', 'request_type', 'loan_amount', 'deposit_amount', 'status', 'due_date', 'installment_number', 'total_deposit_amount', 'rank']
    template_name = 'loan_request_update.html'  # نام قالب HTML برای فرم آپدیت
    success_url = reverse_lazy('loan_request_list')  # پس از به‌روزرسانی به این URL هدایت شود



class LoanRequestDeleteView(DeleteView):
    model = LoanRequest
    template_name = 'loan_request_confirm_delete.html'  # نام قالب HTML برای تایید حذف
    success_url = reverse_lazy('loan_request_list')  # پس از حذف به این URL هدایت شود

def home(request):
    return HttpResponse("Welcome to my site!")


# @api_view(['POST'])
# def login_view(request):
#     try:
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
