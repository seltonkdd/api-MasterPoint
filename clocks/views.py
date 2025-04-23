from rest_framework.viewsets import ModelViewSet

from .serializers import ClockSerializer
from .models import Clock


class ClockViewSet(ModelViewSet):
    serializer_class = ClockSerializer
    queryset = Clock.objects.all()