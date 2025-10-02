# File: wms_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import MyTokenObtainPairView  # <-- 1. Import our custom view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # 2. Use our custom view for the login endpoint
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]