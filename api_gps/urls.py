from django.urls import path

from .views import get_maps_image


urlpatterns = [
    path('get_maps_image/<latitude>/<longitude>/', get_maps_image, name='get_maps_image')
]
