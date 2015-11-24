# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nebschools', '0006_auto_20151119_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='actcomposite',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actenglish',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actmath',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actreading',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='act',
            name='actscience',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
