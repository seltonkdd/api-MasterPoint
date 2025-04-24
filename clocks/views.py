from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from .serializers import ClockSerializer
from .models import Clock
from core.permissions import IsUserOfClock

class ClockViewSet(ModelViewSet):
    serializer_class = ClockSerializer
    queryset = Clock.objects.all()

    permission_classes = [
        DjangoModelPermissions, 
        IsUserOfClock
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff: 
            return Clock.objects.all()
        return Clock.objects.filter(employee__user=user)