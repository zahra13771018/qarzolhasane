<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from .views import LoanRequestUpdateView, LoanRequestDeleteView
from .views import (
    LoanRequestListCreateView, LoanRequestDetailView,
    TransListCreateView, TransDetailView,
    ProfileListCreateView, ProfileDetailView,
    MessageListCreateView, MessageDetailView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Documentation for Qarz al-Hasana project APIs",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@qarzalhasana.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # URLs for loan requests, transactions, profiles, and messages
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

    # Swagger and ReDoc paths for API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Admin and API routes
    path('admin/', admin.site.urls),
    path('api/', include('app_mehr.urls')),
=======
from django.urls import path
# from .views import (
#     LoanRequestListCreateView, LoanRequestDetailView,
#     TransListCreateView, TransDetailView,
#     ProfileListCreateView, ProfileDetailView,
#     MessageListCreateView, MessageDetailView
# )
from app_mehr import views

urlpatterns = [
    # path('loan-requests', views.loan_request_list)
    path('loan-requests/', views.LoanRequestListCreateView.as_view(), name='loan-request-list'),
    # path('loan-requests/<int:pk>/', LoanRequestDetailView.as_view(), name='loan-request-detail'),

    # path('trans/', TransListCreateView.as_view(), name='trans-list'),
    # path('trans/<int:pk>/', TransDetailView.as_view(), name='trans-detail'),

    # path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    # path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

    # path('messages/', MessageListCreateView.as_view(), name='message-list'),
    # path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
>>>>>>> 261e643f41a1a5280e7867d74b276d56f5fe6f17
]
