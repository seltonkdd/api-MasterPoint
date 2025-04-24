from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from employees.models import CustomUser, Employee


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'email', 'is_active', 'is_staff', 'last_login']
    search_fields = ['username', 'email']
    list_filter = ['is_active', 'is_staff']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']