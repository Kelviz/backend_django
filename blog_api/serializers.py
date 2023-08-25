from rest_framework import serializers
from rest_framework.filters import SearchFilter
from .models import Post, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer()
    filter_backends = [SearchFilter]
    search_fields = ['title', 'excerpt',]


    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'author_username',
                  'image', 'featured', 'published', 'created', 'updated', 'pk', 'excerpt', 'category']




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
