from django.urls import path
from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,  # Don't forget to include the update view
    PostDestroyAPIView,
    MyPostListAPIView
)

urlpatterns = [
   
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-detail'),
    
    
    path('posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDestroyAPIView.as_view(), name='post-delete'),
    

    path('me/posts/', MyPostListAPIView.as_view(), name='my-post-list'),
]