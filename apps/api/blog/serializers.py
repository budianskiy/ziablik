from rest_framework import serializers

from apps.blog.models import BlogCategory, Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'image'
        )


class ArticleWriteSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=64))

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'image',
            'tags'
        )


class ArticleReadSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = BlogCategorySerializer()

    class Meta:
        model = Article
        fields = (
            'category',
            'id',
            'user',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'image',
            # 'image_thumbnail',
            'created_at',
            'tags'
        )


