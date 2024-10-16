from django.urls import path
from .views import LoanRequestUpdateView, LoanRequestDeleteView
from .views import (
    LoanRequestListCreateView, LoanRequestDetailView,
    TransListCreateView, TransDetailView,
    ProfileListCreateView, ProfileDetailView,
    MessageListCreateView, MessageDetailView
)

urlpatterns = [
    path('loan-requests/', LoanRequestListCreateView.as_view(), name='loan-request-list'),
    path('loan-requests/<int:pk>/', LoanRequestDetailView.as_view(), name='loan-request-detail'),

    path('trans/', TransListCreateView.as_view(), name='trans-list'),
    path('trans/<int:pk>/', TransDetailView.as_view(), name='trans-detail'),

    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

    path('messages/', MessageListCreateView.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),

    path('loanrequest/<int:pk>/update/', LoanRequestUpdateView.as_view(), name='loanrequest_update'),
    path('loanrequest/<int:pk>/delete/', LoanRequestDeleteView.as_view(), name='loanrequest_delete'),

]
