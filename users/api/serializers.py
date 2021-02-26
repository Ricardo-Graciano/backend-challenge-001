from django.contrib.auth.models import User
from rest_framework import serializers
from topics.models import Topics

class UserSerializer(serializers.ModelSerializer):
    #topics = serializers.PrimaryKeyRelatedField(many=False, queryset=Topics.objects.get())

    class Meta:
        model = User
        fields = ['id', 'username']