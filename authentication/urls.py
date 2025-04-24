from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='obtain_pair_token'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='refresh_token')
]