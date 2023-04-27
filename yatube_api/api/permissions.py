from rest_framework import permissions


class AuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or request.method == 'POST'):
            return True
        return request.user == obj.author
