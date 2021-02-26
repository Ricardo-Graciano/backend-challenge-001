from rest_framework import permissions
from topics.models import Topics

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        try:
            return obj.topic.author == request.user
        except:
            return False

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            topic_urlname = request.resolver_match.kwargs.get('topic_urlname')
            topic = Topics.objects.get(urlname=topic_urlname)
            return topic.author == request.user
        except:
            print(1)
            return False