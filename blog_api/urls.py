from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, FeaturedPostViewSet,  CommentViewSet, CreateCommentViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('featured', FeaturedPostViewSet, basename='featured')

router.register('comments', CommentViewSet,
                basename='comments')
router.register('add-comment', CreateCommentViewSet, basename='add-comment')

urlpatterns = [
    path('', include(router.urls))
]
