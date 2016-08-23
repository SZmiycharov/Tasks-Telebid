# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-19 13:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20160819_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 19, 13, 11, 27, 856441, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 19, 13, 11, 27, 856493, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 19, 13, 11, 27, 866156, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 19, 13, 11, 27, 866208, tzinfo=utc), editable=False),
        ),
    ]