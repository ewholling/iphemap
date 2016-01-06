# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0002_auto_20150130_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='geoid_link',
            field=models.CharField(default=b'', max_length=2000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='study',
            name='platform_geoid_link',
            field=models.CharField(default=b'', max_length=2000),
            preserve_default=True,
        ),
    ]
