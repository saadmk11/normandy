# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 00:03
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations
import normandy.recipes.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='count_limit',
        ),
    ]
