# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170901_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.SlugField(unique=True),
        ),
    ]
