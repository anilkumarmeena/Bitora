# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0032_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]