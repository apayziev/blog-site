from post.models import Post
from django.views import generic
from django.db.models import Q

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        search_query = self.request.GET.get("q")
        if search_query:
            return self.queryset.filter(Q(title__icontains=search_query))
        return self.queryset


