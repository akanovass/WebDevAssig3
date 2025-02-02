# Generated by Django 5.1.2 on 2024-11-10 21:24

import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_author_alter_post_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('published_posts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_commented',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(related_name='categories', to='blog.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
