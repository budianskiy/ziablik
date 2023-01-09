# Generated by Django 4.1.3 on 2023-01-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_meta_description_article_meta_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
    ]
