# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_auto_20170304_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.FloatField(default=10),
        ),
    ]
