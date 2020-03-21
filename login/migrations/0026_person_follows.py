# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_auto_20170403_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='login.Person'),
        ),
    ]