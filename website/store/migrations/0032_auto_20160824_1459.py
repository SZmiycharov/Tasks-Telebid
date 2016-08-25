# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-24 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20160824_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 24, 14, 59, 47, 253054, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 14, 59, 47, 253131, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 24, 14, 59, 47, 266013, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 14, 59, 47, 266063, tzinfo=utc), editable=False),
        ),
    ]
