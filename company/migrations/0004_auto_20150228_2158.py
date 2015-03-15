# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20150228_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
