# Generated by Django 5.0.1 on 2024-02-21 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_verificationcodemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which', to=settings.AUTH_USER_MODEL)),
                ('whom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whom', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Follower',
                'verbose_name_plural': 'Followers',
            },
        ),
    ]