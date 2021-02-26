from rest_framework import viewsets
from users.api import serializers
from django.contrib.auth.models import User

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
