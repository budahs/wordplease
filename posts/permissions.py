from django.utils import timezone

from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return obj.publish_Date <= timezone.now() or obj.owner == request.user or request.user.is_superuser

        return obj.owner == request.user or request.user.is_superuser