# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20170226_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]