from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LoanRequestViewSet,
    TransViewSet,
    ProfileViewSet,
    MessageViewSet,
    LoanRequestListCreateView,
    LoanRequestDetailView,
    TransListCreateView,
    TransDetailView,
    ProfileListCreateView,
    ProfileDetailView,
    MessageListCreateView,
    MessageDetailView,
    LoanRequestUpdateView,
    LoanRequestDeleteView,
    home,
)

# ایجاد یک روتر برای ViewSet ها
router = DefaultRouter()
router.register(r'loan-requests', LoanRequestViewSet)
router.register(r'trans', TransViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),  # شامل URLهای روتر
    path('api/loan-requests/', LoanRequestListCreateView.as_view(), name='loan_request_list_create'),
    path('api/loan-requests/<int:pk>/', LoanRequestDetailView.as_view(), name='loan_request_detail'),
    path('api/trans/', TransListCreateView.as_view(), name='trans_list_create'),
    path('api/trans/<int:pk>/', TransDetailView.as_view(), name='trans_detail'),
    path('api/profiles/', ProfileListCreateView.as_view(), name='profile_list_create'),
    path('api/profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('api/messages/', MessageListCreateView.as_view(), name='message_list_create'),
    path('api/messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('loan-requests/update/<int:pk>/', LoanRequestUpdateView.as_view(), name='loan_request_update'),
    path('loan-requests/delete/<int:pk>/', LoanRequestDeleteView.as_view(), name='loan_request_delete'),
]
