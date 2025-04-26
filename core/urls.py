from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)


urlpatterns = [
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('employees.urls')),
    path('api/v1/', include('clocks.urls')),
    path('api/v1/', include('api_gps.urls')),
    path('', admin.site.urls),
]
