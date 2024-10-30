from django.contrib import admin
from django.urls import path, include
from app_mehr import views


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
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

# urlpatterns = [

#     path('admin/', admin.site.urls),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/', include('app_mehr.urls')),
#     path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

urlpatterns = [
   path('', views.home, name='home'), 
   path('admin/', admin.site.urls), # اضافه کردن مسیر خالی برای صفحه اصلی
   path('api/', include('app_mehr.urls')),  # شامل URLهای اپلیکیشن
   path('loan-requests/update/<int:pk>/', views.LoanRequestUpdateView.as_view(), name='loan_request_update'),
   path('loan-requests/delete/<int:pk>/', views.LoanRequestDeleteView.as_view(), name='loan_request_delete'),
]