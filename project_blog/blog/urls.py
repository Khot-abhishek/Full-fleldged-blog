from django.urls import path
from .views import (about, PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView)


urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('create/', PostCreateView.as_view(), name='blog-create'),
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('about/', about, name="blog-about"),
]
