from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешение: только автор может обновлять или удалять объявление.
    """
    def has_object_permission(self, request, view, obj):
        return request.method in ["GET", "HEAD", "OPTIONS"] or obj.creator == request.user
