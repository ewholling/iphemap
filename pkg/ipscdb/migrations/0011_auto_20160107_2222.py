# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0010_auto_20160107_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='link',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
