# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0042_auto_20170504_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='topic_follows',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to='login.Topic'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic_follows',
            field=models.ManyToManyField(blank=True, related_name='post_followers', to='login.Topic'),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic_follows',
            field=models.ManyToManyField(blank=True, related_name='question_followers', to='login.Topic'),
        ),
    ]