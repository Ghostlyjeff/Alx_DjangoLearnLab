from rest_framework import generics, permissions
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostByCategoryView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Post.objects.filter(category_id=category_id)

class PostByAuthorView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Post.objects.filter(author_id=author_id)


# Create your views here.
