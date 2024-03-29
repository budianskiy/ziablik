from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from config.settings import MEDIA_ROOT


class User(AbstractUser, models.Model):
    phone = PhoneNumberField(verbose_name='Телефон', blank=True, null=True)
    about = models.TextField(verbose_name='Про себя(не обязательно)', default='Тут пока ничего нету')

    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='user/',
        processors=[],
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)]
    )
    about = models.TextField(verbose_name='О себе', blank=True, null=True)
    def image_tag_thumbnail(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}' width='70'>")

    image_tag_thumbnail.short_description = 'Текущий аватар'

    def image_tag(self):
        if self.image:
            if not self.image_thumbnail:
                User.objects.get(id=self.id)
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thumbnail}'>")

    image_tag.short_description = 'Текущий аватар'


