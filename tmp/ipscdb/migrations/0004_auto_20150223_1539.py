# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0003_auto_20150130_2119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gene',
            options={'ordering': ('name', 'pmid')},
        ),
    ]
