# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-14 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20160914_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]