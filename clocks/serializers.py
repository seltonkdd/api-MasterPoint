from rest_framework import serializers

from .models import Clock
from employees.models import Employee


class ClockSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='employee.user.email', read_only=True)

    class Meta:
        model = Clock
        fields = ['id', 'punch', 'employee', 'email']
        read_only_fields = ['employee']

    def create(self, validated_data):
        request = self.context['request']
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            raise serializers.ValidationError('Funcionário não encontrado para o usuário logado.')

        validated_data['employee'] = employee

        return super().create(validated_data)
