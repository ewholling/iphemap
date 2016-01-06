# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0007_figure_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figure',
            name='gene',
        ),
        migrations.AddField(
            model_name='figure',
            name='gene_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
