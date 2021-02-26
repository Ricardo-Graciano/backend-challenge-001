from rest_framework import viewsets, permissions
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from posts import models
from posts.api import serializers
from posts.api.permissions import IsOwnerOrReadOnly, IsOwner

from comments.models import Comments
from topics.models import Topics

class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Posts.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        topic = Topics.objects.get(urlname=self.kwargs.get('topic_urlname'))
        serializer.save(topic_id=topic.id)

    def get_queryset(self):
        if self.kwargs.get('topic_urlname'):
            try:
                topic_urlname = self.kwargs.get('topic_urlname')
                topic = Topics.objects.get(urlname=topic_urlname)
                return models.Posts.objects.filter(topic=topic.id)
            except:
                return models.Posts.objects.none()
        else:
            return super(PostsViewSet, self).get_queryset()

    def retrieve(self, request, topic_urlname=None, pk=None):
        queryset = models.Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk, topic__urlname=topic_urlname)
        post.comments = Comments.objects.filter(post=pk)[0:5]
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data)
