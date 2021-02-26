from rest_framework import serializers
from posts import models
from comments.api.serializers import CommentsSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    topic = serializers.ReadOnlyField(source='topic.id')

    class Meta:
        model = models.Posts
        fields = '__all__'

