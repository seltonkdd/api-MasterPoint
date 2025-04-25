from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('employees.urls')),
    path('api/v1/', include('clocks.urls')),
    path('api/v1/', include('api_gps.urls')),
    path('', admin.site.urls),
]
