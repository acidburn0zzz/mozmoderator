# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-28 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderate', '0004_auto_20170120_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_nda',
            field=models.BooleanField(default=False),
        ),
    ]
