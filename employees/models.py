from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Endereço de email')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome')
    cpf = models.CharField(max_length=15, blank=True, null=True, verbose_name='CPF')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de celular')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.user