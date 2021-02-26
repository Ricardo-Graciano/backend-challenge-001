"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from rest_framework_nested import routers

from helpers.health_check_view import health_check

from topics.api import viewsets as topicsviewsets
from posts.api import viewsets as postsviewsets
from comments.api import viewsets as commentssviewsets
from users import views as usersviews

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'topics', topicsviewsets.TopicsViewSet, basename='topic')

topics_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topics_router.register(r'posts', postsviewsets.PostsViewSet, basename='topic-post')

posts_routers = routers.NestedSimpleRouter(topics_router, r'posts', lookup='post')
posts_routers.register(r'comments', commentssviewsets.CommentsViewSet, basename='topic-post-comment')
###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    path('', include(router.urls)),
    path('', include(topics_router.urls)),
    path('', include(posts_routers.urls)),
]
