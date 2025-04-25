from django.shortcuts import redirect
from core.settings import MAPS_API_KEY


def get_maps_image(request, latitude, longitude):
    zoom = 15
    size = '600x400'
    markers = f'color:red|label:S|{latitude},{longitude}'
    map_type = 'roadmap'
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={size}&markers={markers}&maptype={map_type}&key={MAPS_API_KEY}"

    return redirect(url)
