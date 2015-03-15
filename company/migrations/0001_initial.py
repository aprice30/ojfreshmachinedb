# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=200)),
                ('address_3', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='company.Address')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=('company.address',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('number', models.CharField(max_length=200, blank=True)),
                ('type', models.CharField(default=b'TEL', max_length=3, choices=[(b'TEL', b'Telephone'), (b'MOB', b'Mobile'), (b'FAX', b'Fax')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('contact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='company.Contact')),
                ('is_primary', models.BooleanField(default=False)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
            options={
            },
            bases=('company.contact',),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='company.Address')),
                ('company', models.ForeignKey(to='company.Company')),
            ],
            options={
            },
            bases=('company.address',),
        ),
        migrations.CreateModel(
            name='SiteContact',
            fields=[
                ('contact_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='company.Contact')),
                ('is_primary', models.BooleanField(default=False)),
                ('site', models.ForeignKey(to='company.Site')),
            ],
            options={
            },
            bases=('company.contact',),
        ),
        migrations.AddField(
            model_name='address',
            name='county',
            field=models.ForeignKey(to='company.County'),
            preserve_default=True,
        ),
    ]
