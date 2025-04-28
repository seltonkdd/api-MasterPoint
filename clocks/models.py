from django.db import models

from employees.models import Employee


class Clock(models.Model):
    punch = models.DateTimeField(verbose_name='Batida')
    latitude = models.CharField(max_length=255, null=True, blank=True, verbose_name='Latitude')
    longitude = models.CharField(max_length=255, null=True, blank=True, verbose_name='Longitude')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Funcionário')

    class Meta:
        verbose_name = 'Ponto'
        verbose_name_plural = 'Pontos'

    def __str__(self):
        return f'{self.punch} - {self.employee}'
