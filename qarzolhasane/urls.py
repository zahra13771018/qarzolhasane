"""
URL configuration for qarzolhasane project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_mehr.views import LoanRequestViewSet, TransViewSet, ProfileViewSet, MessageViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app_mehr.views import (
    LoanRequestListCreateView,
    TransListCreateView,
    ProfileListCreateView,
    MessageListCreateView,
    # سایر کلاس‌ها در صورت نیاز
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



# ایجاد یک DefaultRouter
router = DefaultRouter()
router.register(r'loan-requests', LoanRequestViewSet)
router.register(r'transactions', TransViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'messages', MessageViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@domain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('app_mehr.urls')),
    path('api/loan-requests/', LoanRequestListCreateView.as_view(), name='loan_request_list'),
    path('api/trans/', TransListCreateView.as_view(), name='trans_list'),
    path('api/profiles/', ProfileListCreateView.as_view(), name='profile_list'),
    path('api/messages/', MessageListCreateView.as_view(), name='message_list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


