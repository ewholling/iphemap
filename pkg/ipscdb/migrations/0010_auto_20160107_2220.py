# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0009_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='link',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
