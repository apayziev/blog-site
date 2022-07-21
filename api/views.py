from rest_framework import generics
from post.models import Post
from author.models import Author
from api.serializers import PostSerializer, AuthorSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "id"

class AuthorPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'author_id'
   
    def get_queryset(self):
        author_id = self.kwargs.get("author_id")
        return self.queryset.filter(author_id=author_id)

class FeaturedThisMonthAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return self.queryset.filter(is_featured=True)

class RecentlyPostedAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    
class TopAuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        return self.queryset.filter(is_top=True)

class PopularPostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return self.queryset.filter(is_popular=True)