# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('authority', models.CharField(max_length=1, choices=[(b'0', b'super'), (b'1', b'gene')])),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('abstract', models.TextField(max_length=1000)),
                ('stock', models.IntegerField(default=0)),
                ('borrowed', models.IntegerField(default=0)),
                ('indate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('sex', models.CharField(max_length=1, choices=[(b'0', b'm'), (b'1', b'f')])),
                ('rtype', models.CharField(max_length=45)),
                ('bar_code', models.CharField(max_length=45)),
                ('birthday', models.DateField()),
                ('paper_type', models.CharField(max_length=45)),
                ('paper_number', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Recoders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lend_date', models.DateField()),
                ('return_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=1, choices=[(b'0', b'lend'), (b'1', b'return'), (b'2', b'exceed')])),
                ('limit', models.IntegerField(default=90)),
                ('book', models.ForeignKey(to='modles.Books')),
                ('reader', models.ForeignKey(to='modles.Reader')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(to='modles.Category'),
        ),
    ]
