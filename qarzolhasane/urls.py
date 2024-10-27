from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app_mehr.urls')),  # به درستی به urls.py در برنامه شما ارجاع می‌دهد
]
