# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0002_auto_20150227_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='bought_exchange_rate',
            field=models.DecimalField(null=True, verbose_name=b'Exchange Rate', max_digits=7, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='sold_exchange_rate',
            field=models.DecimalField(null=True, verbose_name=b'Exchange Rate', max_digits=7, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
