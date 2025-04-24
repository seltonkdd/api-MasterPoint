from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    permission_classes = [
        DjangoModelPermissions, 
        IsAdminUser
    ]