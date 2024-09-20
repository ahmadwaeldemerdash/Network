# Generated by Django 5.1 on 2024-09-20 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_rename_follows_follow_followed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='network.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
