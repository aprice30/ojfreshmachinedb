# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150222_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, to='company.Country', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.CharField(max_length=10, verbose_name=b'Post Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companycontact',
            name='is_primary',
            field=models.BooleanField(default=False, verbose_name=b'Is Primary?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sitecontact',
            name='is_primary',
            field=models.BooleanField(default=False, verbose_name=b'Is Primary?'),
            preserve_default=True,
        ),
    ]
