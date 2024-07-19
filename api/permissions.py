from rest_framework import permissions


class IsOwnerOrRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.owner == request.user)
