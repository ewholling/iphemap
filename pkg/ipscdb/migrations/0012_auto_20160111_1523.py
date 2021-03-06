# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0011_auto_20160107_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='experiment_type',
        ),
        migrations.AddField(
            model_name='study',
            name='control_patients',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='disease',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='disease_patients',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='reprogramming_type',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='snp',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='utilization',
            field=models.BooleanField(default=False),
        ),
    ]
