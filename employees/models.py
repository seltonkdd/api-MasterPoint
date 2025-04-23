from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Endereço de email')
    is_staff = models.BooleanField(default=False, verbose_name='É admin')
    is_active = models.BooleanField(default=True, verbose_name='É ativo')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, verbose_name='Usuário', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Nome', null=False)
    cpf = models.CharField(max_length=15, blank=True, null=True, verbose_name='CPF', unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de celular')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name