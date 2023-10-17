from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Checking if the user is the object's owner.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner