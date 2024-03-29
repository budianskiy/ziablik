from apps.main.mixins import MetaTagMixin
from apps.user.models import User
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from config.settings import MEDIA_ROOT

# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=255)
    #image = models.ImageField(verbose_name='Изображение', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категория блога'


    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Изображение'


    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Изображение'


class Article(MetaTagMixin):
    category = models.ForeignKey(to=BlogCategory, verbose_name='Категория', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью', null = True, blank = True)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name = 'Дата публикации')
    tags = models.ManyToManyField(to = 'Tag', verbose_name = 'Теги', blank = True)

    author = models.CharField(verbose_name='Автор', max_length=255, null=True, blank=True)
    author_image = ProcessedImageField(
        verbose_name='Аватарка автора',
        upload_to='blog/article/',
        processors=[],
        null=True,
        blank=True
    )


    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[],
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now = True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add = True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Tag(MetaTagMixin):
    name = models.CharField(verbose_name='Тег', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comments(models.Model):
    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Автор', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name='Имя', max_length=255)
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Текст')
    is_checked = models.BooleanField(verbose_name='проверен', default=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
