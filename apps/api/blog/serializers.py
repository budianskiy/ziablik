from rest_framework import serializers
from apps.blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
            'slug'
        )
