from rest_framework import permissions

from users.models import User


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Вы не имеете доступа к этой подборке'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class AdUpdatePermission(permissions.BasePermission):
    message = 'Вы не имеете доступа к этому объявлению'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [User.ADMIN,
                                                               User.MODERATOR]:
            return True
        return False
