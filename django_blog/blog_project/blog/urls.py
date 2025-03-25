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
from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
path('profile/edit/', profile_edit_view, name='profile_edit'),
