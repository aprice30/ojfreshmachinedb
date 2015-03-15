# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('type', models.CharField(default=b'COMMENT', max_length=11, choices=[(b'COMMENT', b'Comment'), (b'MAINTENANCE', b'Maintenance')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=32, blank=True)),
                ('invoice_number', models.CharField(max_length=32, blank=True)),
                ('invoice_date', models.DateField(null=True, blank=True)),
                ('bought_date', models.DateField(null=True, blank=True)),
                ('supplier_invoice', models.CharField(max_length=32, blank=True)),
                ('bought_price', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('bought_exchange_rate', models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)),
                ('sold_price', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('sold_exchange_rate', models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)),
                ('manufacture_date', models.DateField(null=True, blank=True)),
                ('last_pat', models.DateField(null=True, blank=True)),
                ('next_pat', models.DateField(null=True, blank=True)),
                ('last_maintenance', models.DateField(null=True, blank=True)),
                ('next_maintenance', models.DateField(null=True, blank=True)),
                ('on_loan', models.BooleanField(default=False)),
                ('is_fixed_asset', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MachineModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_model',
            field=models.ForeignKey(to='machine.MachineModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='machine',
            name='site',
            field=models.ForeignKey(to='company.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='machine',
            name='supplier',
            field=models.ForeignKey(blank=True, to='machine.Supplier', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ledger',
            name='machine',
            field=models.ForeignKey(to='machine.Machine'),
            preserve_default=True,
        ),
    ]
