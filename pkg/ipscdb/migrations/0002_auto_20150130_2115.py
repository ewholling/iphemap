# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='geoid_link',
        ),
        migrations.RemoveField(
            model_name='study',
            name='platform_geoid_link',
        ),
    ]
