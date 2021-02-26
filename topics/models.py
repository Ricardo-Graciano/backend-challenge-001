from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Topics(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='topic_author', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    urlname = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)