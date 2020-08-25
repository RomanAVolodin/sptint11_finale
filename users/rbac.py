from rest_framework.permissions import SAFE_METHODS, BasePermission


class AnyoneCanSeeListAdminCanEdit(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin
