from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_mehr.views import ProfileViewSet, LoanRequestViewSet, TransViewSet, MessageViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# ایجاد یک روتر پیش‌فرض
router = DefaultRouter()
# اضافه کردن ViewSets به روتر
router.register(r'profiles', ProfileViewSet)
router.register(r'loan-requests', LoanRequestViewSet)
router.register(r'trans', TransViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),  # آدرس برای ورود به بخش مدیریت
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
   path('api/', include(router.urls)),  # شامل URLهای روتر
   path('api/profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile_list_create'),
   path('api/profiles/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='profile_detail'),
   path('api/messages/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='message_list_create'),
   path('api/messages/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='message_detail'),
   path('api/loan-requests/', LoanRequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='loan_request_list_create'),
   path('api/loan-requests/<int:pk>/', LoanRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='loan_request_detail'),
   path('api/trans/', TransViewSet.as_view({'get': 'list', 'post': 'create'}), name='trans_list_create'),
   path('api/trans/<int:pk>/', TransViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='trans_detail'),
   
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
