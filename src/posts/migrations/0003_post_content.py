# Generated by Django 2.2.7 on 2020-05-29 17:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
        ),
    ]
