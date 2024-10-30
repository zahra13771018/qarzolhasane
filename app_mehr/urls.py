# from django.urls import path, include
# from . import views 
# from rest_framework.routers import DefaultRouter
# from .views import (
#     LoanRequestViewSet,
#     TransViewSet,
#     ProfileViewSet,
#     MessageViewSet,
#     LoanRequestListCreateView,
#     LoanRequestDetailView,
#     TransListCreateView,
#     TransDetailView,
#     ProfileListCreateView,
#     ProfileDetailView,
#     MessageListCreateView,
#     MessageDetailView,
#     LoanRequestUpdateView,
#     LoanRequestDeleteView,
#     home,  # اضافه کردن view home
# )

# # ایجاد یک روتر برای ViewSet ها
# router = DefaultRouter()
# router.register(r'loan-requests', LoanRequestViewSet)
# router.register(r'trans', TransViewSet)
# router.register(r'profiles', ProfileViewSet)
# router.register(r'messages', MessageViewSet)

# # urlpatterns = [
# #     path('', home, name='home'),  # اضافه کردن مسیر خالی برای صفحه اصلی
# #     path('api/', include(router.urls)),  # شامل URLهای روتر
# #     path('api/loan-requests/', LoanRequestListCreateView.as_view(), name='loan_request_list_create'),
# #     path('api/loan-requests/<int:pk>/', LoanRequestDetailView.as_view(), name='loan_request_detail'),
# #     path('api/trans/', TransListCreateView.as_view(), name='trans_list_create'),
# #     path('api/trans/<int:pk>/', TransDetailView.as_view(), name='trans_detail'),
# #     path('api/profiles/', ProfileListCreateView.as_view(), name='profile_list_create'),
# #     path('api/profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
# #     path('api/messages/', MessageListCreateView.as_view(), name='message_list_create'),
# #     path('api/messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
# #     path('loan-requests/update/<int:pk>/', LoanRequestUpdateView.as_view(), name='loan_request_update'),
# #     path('loan-requests/delete/<int:pk>/', LoanRequestDeleteView.as_view(), name='loan_request_delete'),
    
# # ]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('loan-requests/', views.LoanRequestListCreateView.as_view(), name='loan_request_list_create'),
#     path('loan-requests/<int:pk>/', views.LoanRequestDetailView.as_view(), name='loan_request_detail'),
#     path('trans/', views.TransListCreateView.as_view(), name='trans_list_create'),
#     path('trans/<int:pk>/', views.TransDetailView.as_view(), name='trans_detail'),
#     path('profiles/', views.ProfileListCreateView.as_view(), name='profile_list_create'),
#     path('profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
#     path('messages/', views.MessageListCreateView.as_view(), name='message_list_create'),
#     path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
# ]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet,  LoanRequestViewSet, TransViewSet, MessageViewSet
from . import views

router = DefaultRouter()
# اضافه کردن ViewSets به روتر (در صورت استفاده از ViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'loan-requests', LoanRequestViewSet)
router.register(r'trans', TransViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),  # شامل URLهای روتر
    # یا اگر از ویوهای عادی استفاده می‌کنید به این صورت بنویسید:
    path('api/profiles/', views.ProfileListCreateView.as_view(), name='profile_list_create'),
    path('api/profiles/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('api/messages/', views.MessageListCreateView.as_view(), name='message_list_create'),
    path('api/messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('api/loan-requests/', views.LoanRequestListCreateView.as_view(), name='loan_request_list_create'),
    path('api/loan-requests/<int:pk>/', views.LoanRequestDetailView.as_view(), name='loan_request_detail'),
    path('api/trans/', views.TransListCreateView.as_view(), name='trans_list_create'),
    path('api/trans/<int:pk>/', views.TransDetailView.as_view(), name='trans_detail'),
]
