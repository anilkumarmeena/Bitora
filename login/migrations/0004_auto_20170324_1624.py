# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_person_display_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
