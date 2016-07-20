# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 09:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_group_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.AddField(
            model_name='gituser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
    ]