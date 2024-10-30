from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_mehr.views import ProfileViewSet, LoanRequestViewSet, TransViewSet, MessageViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ایجاد یک روتر پیش‌فرض
router = DefaultRouter()
# اضافه کردن ViewSets به روتر
router.register(r'profiles', ProfileViewSet)
router.register(r'loan-requests', LoanRequestViewSet)
router.register(r'trans', TransViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),  # آدرس برای ورود به بخش مدیریت
   path('api/', include(router.urls)),  # شامل URLهای روتر
    # اگر از ویوهای عادی استفاده می‌کنید به این صورت بنویسید:
   path('api/profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile_list_create'),
   path('api/profiles/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='profile_detail'),
   path('api/messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message_list_create'),
   path('api/messages/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='message_detail'),
   path('api/loan-requests/', LoanRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='loan_request_list_create'),
   path('api/loan-requests/<int:pk>/', LoanRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='loan_request_detail'),
   path('api/trans/', TransViewSet.as_view({'get': 'list', 'post': 'create'}), name='trans_list_create'),
   path('api/trans/<int:pk>/', TransViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='trans_detail'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
