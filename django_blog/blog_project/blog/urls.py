from django.urls import path
from .views import (
    PostListCreateView, PostDetailView, CategoryListView, 
    PostByCategoryView, PostByAuthorView
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('posts/category/<int:category_id>/', PostByCategoryView.as_view(), name='posts-by-category'),
    path('posts/author/<int:author_id>/', PostByAuthorView.as_view(), name='posts-by-author'),
]
