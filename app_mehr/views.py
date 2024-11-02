from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import LoanRequest, Profile, Message, Trans
from .serializers import ProfileSerializer, MessageSerializer, TransSerializer, LoanRequestSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)

def home(request):
    return HttpResponse("Welcome to my site!")


class LoanRequestViewSet(viewsets.ModelViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [IsAuthenticated]

class LoanRequestListCreateView(generics.ListCreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
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
    fields = ['loan_type', 'request_type', 'loan_amount', 'deposit_amount', 'status', 'due_date']
    template_name = 'loan_request_update.html'  # نام قالب HTML برای فرم آپدیت
    success_url = reverse_lazy('loan_request_list')  # پس از به‌روزرسانی به این URL هدایت شود

class LoanRequestDeleteView(DeleteView):
    model = LoanRequest
    template_name = 'loan_request_confirm_delete.html'  # نام قالب HTML برای تایید حذف
    success_url = reverse_lazy('loan_request_list')  # پس از حذف به این URL هدایت شود


