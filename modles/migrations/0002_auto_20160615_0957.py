# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoders',
            name='return_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
