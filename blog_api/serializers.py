from rest_framework import serializers
from .models import Post, Category, Comment


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    image = serializers.SerializerMethodField()

    def get_image(self, post):
        if post.image:
            return post.image.url
        return None


    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'author_username',
                  'image', 'featured', 'published', 'created', 'updated', 'pk', 'excerpt', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
