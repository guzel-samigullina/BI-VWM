# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20170227_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='idf',
            field=models.FloatField(default=0),
        ),
    ]
