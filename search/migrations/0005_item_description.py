# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 18:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default=datetime.date(2017, 2, 2), max_length=5000),
            preserve_default=False,
        ),
    ]
