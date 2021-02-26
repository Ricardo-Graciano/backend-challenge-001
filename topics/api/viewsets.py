from rest_framework import viewsets, permissions
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from topics import models
from topics.api import serializers
from topics.api.permissions import IsOwnerOrReadOnly

from posts.models import Posts
from posts.api.serializers import PostSerializer


class TopicsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TopicSerializer
    queryset = models.Topics.objects.all()
    lookup_field = 'urlname'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, urlname=None):
        queryset = models.Topics.objects.all()
        topic = get_object_or_404(queryset, urlname=urlname)
        topic.posts = Posts.objects.filter(topic__urlname=urlname)[0:5]
        serializer = serializers.TopicSerializer(topic)
        return Response(serializer.data)
