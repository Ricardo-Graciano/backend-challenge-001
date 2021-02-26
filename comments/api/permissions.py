from rest_framework import permissions
from topics.models import Topics
from topics.models import Topics
from posts.models import Posts

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            return obj.post.topic.author == request.user
        except:
            return False