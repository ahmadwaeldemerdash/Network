# Generated by Django 5.1 on 2024-09-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.IntegerField(default=0),
        ),
    ]
