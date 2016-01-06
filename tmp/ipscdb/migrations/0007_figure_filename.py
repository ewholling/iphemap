# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0006_auto_20150303_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='figure',
            name='filename',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
