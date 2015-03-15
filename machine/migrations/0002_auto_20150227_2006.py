# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='bought_date',
            field=models.DateField(null=True, verbose_name=b'Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='bought_exchange_rate',
            field=models.DecimalField(null=True, verbose_name=b'Exchange Rate', max_digits=6, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='bought_price',
            field=models.DecimalField(null=True, verbose_name=b'Price', max_digits=7, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='invoice_date',
            field=models.DateField(null=True, verbose_name=b'Invoice Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='invoice_number',
            field=models.CharField(max_length=32, verbose_name=b'Invoice No.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='is_fixed_asset',
            field=models.BooleanField(default=False, verbose_name=b'Is Fixed Asset'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='last_maintenance',
            field=models.DateField(null=True, verbose_name=b'Last Maintenance', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='last_pat',
            field=models.DateField(null=True, verbose_name=b'Last PAT', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='machine_model',
            field=models.ForeignKey(verbose_name=b'Model', to='machine.MachineModel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='manufacture_date',
            field=models.DateField(null=True, verbose_name=b'Manufacture Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='next_maintenance',
            field=models.DateField(null=True, verbose_name=b'Next Maintenance', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='next_pat',
            field=models.DateField(null=True, verbose_name=b'Next PAT', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='on_loan',
            field=models.BooleanField(default=False, verbose_name=b'On Loan'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='serial',
            field=models.CharField(max_length=32, verbose_name=b'Serial #'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='sold_exchange_rate',
            field=models.DecimalField(null=True, verbose_name=b'Exchange Rate', max_digits=6, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='sold_price',
            field=models.DecimalField(null=True, verbose_name=b'Price', max_digits=7, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='supplier_invoice',
            field=models.CharField(max_length=32, verbose_name=b'Supplier Invoice', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machinemodel',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
