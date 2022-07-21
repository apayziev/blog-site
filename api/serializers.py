from post.models import Post, Category, Tag
from author.models import Author
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    tag = TagSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'