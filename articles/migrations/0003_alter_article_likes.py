# Generated by Django 4.2.1 on 2023-05-25 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_rename_author_article_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
