# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20160706_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owener', to=settings.AUTH_USER_MODEL, verbose_name='owener'),
            preserve_default=False,
        ),
    ]
