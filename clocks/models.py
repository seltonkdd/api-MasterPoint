from django.db import models

from employees.models import Employee


class Clock(models.Model):
    punch = models.DateTimeField(verbose_name='Batida')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Funcionário')

    class Meta:
        verbose_name = 'Ponto'
        verbose_name_plural = 'Pontos'

    def __str__(self):
        return f'{self.punch} - {self.employee}'

