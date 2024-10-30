from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, LoanRequestViewSet, TransViewSet, MessageViewSet

# ایجاد یک روتر پیش‌فرض
router = DefaultRouter()
# اضافه کردن ViewSets به روتر
router.register(r'profiles', ProfileViewSet)
router.register(r'loan-requests', LoanRequestViewSet)
router.register(r'trans', TransViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # شامل URLهای روتر
]
