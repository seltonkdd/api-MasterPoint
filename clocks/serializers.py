from rest_framework import serializers

from .models import Clock
from employees.models import Employee


class ClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clock
        fields = '__all__'
        read_only_fields = ['employee']

    def create(self, validated_data):
        request = self.context['request']
        try:
            employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            raise serializers.ValidationError('Funcionário não encontrado para o usuário logado.')

        validated_data['employee'] = employee

        return super().create(validated_data)
