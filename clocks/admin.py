from django.contrib import admin

from .models import Clock


@admin.register(Clock)
class ClockAdmin(admin.ModelAdmin):
    list_display = ['employee', 'punch', 'latitude', 'longitude']
    search_fields = ['employee']
    list_filter = ['employee',]
