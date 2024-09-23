from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.groups.filter(name="doctors").exists()
