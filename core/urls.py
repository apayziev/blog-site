from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("post.urls")),
    path("api/", include("api.urls")),
    path('contact-us/', include('common.urls')),
]
