# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('disease', models.CharField(max_length=200)),
                ('snp', models.CharField(max_length=200)),
                ('pmid', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('disease', 'snp'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phenotype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('domain', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('description',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_author', models.CharField(max_length=1000)),
                ('species', models.CharField(max_length=1000)),
                ('year', models.IntegerField(default=0)),
                ('experiment_type', models.CharField(max_length=1000)),
                ('starting_cell_type', models.CharField(max_length=1000)),
                ('target_cell_type', models.CharField(max_length=1000)),
                ('geoid', models.CharField(max_length=1000)),
                ('platform_name', models.CharField(max_length=1000)),
                ('platform_geo_id', models.CharField(max_length=1000)),
                ('pmid', models.IntegerField(default=0)),
                ('geoid_link', models.CharField(max_length=2000)),
                ('platform_geoid_link', models.CharField(max_length=2000)),
            ],
            options={
                'ordering': ('year',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gene',
            name='phenotypes',
            field=models.ManyToManyField(to='ipscdb.Phenotype'),
            preserve_default=True,
        ),
    ]
