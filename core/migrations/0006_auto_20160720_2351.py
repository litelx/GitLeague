# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160712_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gituser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='EMail'),
        ),
    ]
