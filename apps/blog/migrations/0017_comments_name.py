# Generated by Django 4.1.3 on 2023-02-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_comments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
