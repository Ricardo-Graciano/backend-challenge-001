from rest_framework import viewsets, permissions

from comments import models
from comments.api import serializers
from comments.api.permissions import  IsOwnerOrReadOnly, isOwner

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer
    queryset = models.Comments.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.kwargs.get('post_pk'):
            post_pk = self.kwargs.get('post_pk')
            return models.Comments.objects.filter(post=post_pk)
        else:
            return super(CommentsViewSet, self).get_queryset()

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs.get('post_pk'))