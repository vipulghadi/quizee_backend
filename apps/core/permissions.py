from  rest_framework.permissions import BasePermission
from apps.account.enums import RoleEnum

class IsSuperAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser and request.user.role==RoleEnum.SUPER_ADMIN)

class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user.role==RoleEnum.ADMIN)

class IsSME(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user.role==RoleEnum.SME)


class IsAdminOrSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.role in [RoleEnum.SUPER_ADMIN, RoleEnum.ADMIN]
        )