from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = 'Изменение чужого контента запрещено!'

    def object_permission(self, request, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
