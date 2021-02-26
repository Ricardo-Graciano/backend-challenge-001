#from django.contrib.auth.models import Topic
from rest_framework import serializers
from topics import models
from posts.api.serializers import PostSerializer

class TopicSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = models.Topics
        fields = '__all__'
        lookup_field = 'urlname'

