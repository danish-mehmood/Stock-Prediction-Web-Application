# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-14 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0006_auto_20160414_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='dividend_yield',
            field=models.CharField(max_length=20, null=True),
        ),
    ]