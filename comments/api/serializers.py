from rest_framework import serializers

from comments import models

class CommentsSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.id')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = models.Comments
        fields = '__all__'
