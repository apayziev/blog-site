from api.views import *
from django.urls import path


app_name = "api"


urlpatterns = [
    path("posts/", PostAPIView.as_view(), name="posts"),
    path("authors/<int:id>/", AuthorDetailAPIView.as_view(), name="authors"),
    path("authors/<int:author_id>/posts", AuthorPostsView.as_view(), name="authors"),
    path("posts/featured/", FeaturedThisMonthAPIView.as_view(), name="featured"),
    path("posts/recently-posted/", RecentlyPostedAPIView.as_view(), name="recent"),
    path("authors/top-authors/", TopAuthorAPIView.as_view(), name="top"),
    path("posts/popular-posts/", PopularPostApiView.as_view(), name="popular"),

]
