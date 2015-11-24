# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0008_auto_20151122_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropout',
            name='agencykey',
            field=models.ForeignKey(to='nebschools.District'),
        ),
    ]
