# Generated by Django 5.1 on 2024-09-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_remove_user_followers_remove_user_follows_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follows',
            new_name='followed',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='follower',
        ),
    ]
