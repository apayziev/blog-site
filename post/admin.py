from django.contrib import admin
from .models import Category, Post, Tag

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
