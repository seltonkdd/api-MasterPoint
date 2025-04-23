from rest_framework.viewsets import ModelViewSet

from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()