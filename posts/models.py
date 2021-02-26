from django.db import models
from topics.models import Topics
from django.contrib.contenttypes.fields import GenericRelation

class Posts(models.Model):
    readonly_fields= ['topic']

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topics, related_name='posts_topic', on_delete=models.CASCADE)
