
# Generated by Django 4.1.3 on 2023-01-20 14:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',

            field=models.TextField(blank=True, null=True, verbose_name='О себе'),

        ),
    ]
