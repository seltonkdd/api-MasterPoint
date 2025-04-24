from rest_framework.permissions import BasePermission


class IsUserOfClock(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.employee.user