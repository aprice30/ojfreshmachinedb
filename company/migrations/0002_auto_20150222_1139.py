# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_1',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_3',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='county',
            field=models.ForeignKey(blank=True, to='company.County', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='town',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
