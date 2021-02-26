from django.db import models
from posts.models import Posts

class Comments(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Posts, related_name='comments_post', on_delete=models.CASCADE)
