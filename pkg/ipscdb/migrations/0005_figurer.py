# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipscdb', '0004_auto_20150223_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Figurer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=200)),
                ('hindex', models.IntegerField(default=0)),
                ('pmid', models.IntegerField(default=0)),
                ('gene', models.ForeignKey(to='ipscdb.Gene')),
            ],
            options={
                'ordering': ('hindex',),
            },
            bases=(models.Model,),
        ),
    ]
